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
    
    subgraph Onboarding [Flujo de Establecimiento en Tiquetera]
        H --> I[Usuario abre enlace y es redirigido a Vista Web Tiquetera]
        I --> J[Usuario define su nueva contraseña]
        J --> K[Tiquetera valida Token y guarda clave local]
    end

    K --> L[Tiquetera dispara Fan-Out a API]
    
    N[Cambio de contraseña habitual] --> O[(BD Tiquetera)]
    O --> P[Tiquetera envía a API]
    P --> L
    
    L --> M{API distribuye a 5 apps}
    
    M -->|GoC| S1[GoC recibe datos/actualización]
    M -->|Krono| S2[Krono recibe datos/actualización]
    M -->|Trazum| S3[Trazum recibe datos/actualización]
    M -->|Tiquetera| S4[Tiquetera recibe datos/actualización]
    M -->|Wiki.js / App 5| S5[App 5 recibe /actualización vía GraphQL]
    
    S1 --> DB1[(Base de Datos GoC)]
    S2 --> DB2[(Base de Datos Krono)]
    S3 --> DB3[(Base de Datos Trazum)]
    S4 --> DB4[(Base de Datos Tiquetera)]
    S5 --> DB5[(Base de Datos App 5)]
    
    classDef default fill:#404040,stroke:#e5e5e5,stroke-width:1px,color:#ffffff
