```mermaid
flowchart TD
    classDef usuario fill:#8e44ad,stroke:#9b59b6,stroke-width:2px,color:#fff
    classDef sso fill:#27ae60,stroke:#2ecc71,stroke-width:2px,color:#fff
    classDef emergencia fill:#c0392b,stroke:#e74c3c,stroke-width:2px,color:#fff
    classDef db fill:#2c3e50,stroke:#34495e,stroke-width:2px,color:#fff

    U([Usuario en Navegador]):::usuario

    subgraph Fase_1 [1. Fan-Out Original: Carga de Respaldo]
        R1[Registro o Cambio de Clave] --> R2[API despacha Fan-Out asincrono]
        R2 -.->|Replica hashes pbkdf2_sha256| BD_GoC[(BD GoC)]:::db
        R2 -.->|Replica hashes pbkdf2_sha256| BD_Krono[(BD Krono)]:::db
    end

    subgraph Fase_2 [2. Flujo Normal: Autenticacion Descentralizada SSO]
        U -->|1. Ingresa credenciales| Login[Portal de Login API]
        Login --> API_Central{API Central en linea?}:::sso
        
        API_Central -->|SI: Valida usuario| GeneraTokens[Emite Tokens]
        GeneraTokens -->|Access en RAM y Refresh en Cookie| U
        
        U -->|2. Navega a app| Middleware[Middleware de la App Web]
        Middleware --> ValidaFirma{Token valido?}
        ValidaFirma -->|Si, vigente| AccesoOK[Acceso Concedido]
        
        ValidaFirma -->|No, expiro| Error401[Error 401 HTTP]
        Error401 -->|3. Interceptor web| Refrescar[Pide nuevo token silenciosamente]
        Refrescar -->|Envia Cookie segura| API_Central
    end

    subgraph Fase_3 [3. Plan B: Caida del SSO]
        API_Central -->|NO: Error o Timeout| Caida[Se congela validacion central]:::emergencia
        Caida -->|Usuario va a URL alterna| LoginEmergencia[Portal de Emergencia Local]
        LoginEmergencia -->|App consulta su BD| BD_Local{Valida en BD Local}
        BD_Krono -.->|Suministra datos a| BD_Local
        BD_Local -->|Hash coincide| AccesoDegradado[Acceso en Modo Emergencia]
    end
