---
config:
  layout: elk
---
flowchart TD
    A[Se registra usuario] --> B[(Biométrico DB)]
    B --> C[API consulta datos]
    C --> D[Tiquetera sincroniza datos nuevos]
    D --> E[(Base de Datos Central)]
    E --> F[Creación de usuarios]
    F --> G[Envía datos a API]
    G --> H{API distribuye a 5 apps}
    
    N[Cambio de contraseña] --> O[(BD Tiquetera)]
    O --> P[Tiquetera envía a API]
    P --> H
    
    H -->|GoC| I[GoC recibe datos/actualización]
    H -->|Krono| J[Krono recibe datos/actualización]
    H -->|Trazum| K[Trazum recibe datos/actualización]
    H -->|Tiquetera| L[Tiquetera recibe datos/actualización]
    H -->|Nueva App| W[App 5 recibe datos/actualización]
    
    I --> DB1[(Base de Datos GoC)]
    J --> DB2[(Base de Datos Krono)]
    K --> DB3[(Base de Datos Trazum)]
    L --> DB4[(Base de Datos Tiquetera)]
    W --> DB5[(Base de Datos App 5)]
    
    classDef registro fill:#f0fdf4,stroke:#4ade80
    classDef biometric fill:#eef2ff,stroke:#818cf8
    classDef api fill:#f0f9ff,stroke:#38bdf8
    classDef sync fill:#fef2f2,stroke:#f87171
    classDef app fill:#f5f3ff,stroke:#a78bfa
    classDef database fill:#fdf4ff,stroke:#e879f9
    classDef password fill:#fff7ed,stroke:#fb923c
    
    class A,F registro
    class B,E,O,DB1,DB2,DB3,DB4,DB5 database
    class C,G,H,P api
    class D,N sync
    class I,J,K,L,W app
