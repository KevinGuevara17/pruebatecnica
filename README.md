---
config:
  layout: elk
  theme: dark
---
flowchart TD
    A[Se registra usuario] --> B[(Biométrico DB)]
    B --> C[API consulta datos]
    C --> D[Tiquetera sincroniza datos nuevos]
    D --> E[(Base de Datos tiquetera)]
    E --> F[Creación de usuarios con estado pendiente]
    F --> G[Sistema genera Token de Activación]
    G --> H[Envía Correo Electrónico con Enlace Seguro]
    
    subgraph Onboarding [Flujo de Establecimiento de Contraseña]
        H --> I[Usuario abre enlace y define Contraseña]
        I --> J[Tiquetera valida Token y guarda clave local]
    end

    J --> K[Tiquetera dispara Fan-Out a API]
    
    N[Cambio de contraseña habitual] --> O[(BD Tiquetera)]
    O --> P[Tiquetera envía a API]
    P --> K
    
    K --> L{API distribuye a 5 apps}
    
    L -->|GoC| M[GoC recibe datos/actualización]
    L -->|Krono| N1[Krono recibe datos/actualización]
    L -->|Trazum| Q[Trazum recibe datos/actualización]
    L -->|Tiquetera| R[Tiquetera recibe datos/actualización]
    L -->|Wiki.js / App 5| W[App 5 recibe /actualización vía GraphQL]
    
    M --> DB1[(Base de Datos GoC)]
    N1 --> DB2[(Base de Datos Krono)]
    Q --> DB3[(Base de Datos Trazum)]
    R --> DB4[(Base de Datos Tiquetera)]
    W --> DB5[(Base de Datos App 5)]
    
    classDef default fill:#404040,stroke:#e5e5e5,stroke-width:1px,color:#ffffff
