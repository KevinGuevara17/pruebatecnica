```mermaid
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
        H --> I[Usuario abre enlace en vista web Tiquetera]
        I --> J[Usuario ingresa su nueva contraseña]
        J --> K[Tiquetera envía credenciales a API]
        K --> L[API valida Token y actualiza clave]
    end

    L --> M[API dispara Fan-Out masivo]
    
    N[Cambio de contraseña habitual] --> O[(BD Tiquetera)]
    O --> P[Tiquetera envía a API]
    P --> M
    
    M --> Q{API distribuye a 5 apps}
    
    Q -->|GoC| S1[GoC recibe datos/actualización]
    Q -->|Krono| S2[Krono recibe datos/actualización]
    Q -->|Trazum| S3[Trazum recibe datos/actualización]
    Q -->|Tiquetera| S4[Tiquetera recibe datos/actualización]
    Q -->|Wiki.js / App 5| S5[App 5 recibe /actualización vía GraphQL]
    
    S1 --> DB1[(Base de Datos GoC)]
    S2 --> DB2[(Base de Datos Krono)]
    S3 --> DB3[(Base de Datos Trazum)]
    S4 --> DB4[(Base de Datos Tiquetera)]
    S5 --> DB5[(Base de Datos App 5)]
    
    classDef default fill:#404040,stroke:#e5e5e5,stroke-width:1px,color:#ffffff
