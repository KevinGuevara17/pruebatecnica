# 🎫 Tiquetera — Mesa de Ayuda de TI & Gestión de Inventario

Mesa de ayuda corporativa de **Tecnología de Industrias Goya Incol**. Un portal unificado donde cualquier empleado radica sus requerimientos o incidentes, inspecciona el estado de su caso en tiempo real y gestiona su inventario de activos electrónicos, mientras el equipo de TI prioriza, asigna, conversa, audita y resuelve.

---

## 🚀 Tecnologías Principales Utilizadas

### 🛠️ Backend & Tiempo Real
- **Python 3.12 & Django 5.0+**: Núcleo robusto para la lógica de negocio, ORM, auditoría append-only y seguridad RBAC/ABAC.
- **Django Channels 4.0+ & Daphne (ASGI)**: Comunicación bidireccional en tiempo real mediante WebSockets (refresco de SLA, chat en vivo y actualización instantánea de estados).
- **PostgreSQL 16**: Base de datos relacional transaccional (con soporte SQLite para pruebas locales).
- **Redis 7**: Broker de mensajes en memoria y capa de canales para WebSockets de Channels.
- **Pillow (Image Sanitization)**: Re-codificación desinfectante de adjuntos a WebP para eliminar EXIF y payloads.
- **Hashids**: Ofuscación transparente de claves primarias (PKs) en URLs (`<hashid:pk>`).

### 🎨 Frontend & Diseño
- **Tailwind CSS 4.0**: Sistema de diseño con tokens semánticos (Terracota `#9C5F3A` / Azul Oscuro `#0F172A`).
- **daisyUI 5.7 & Flowbite**: Componentes responsivos, modales integrados, tablas interactivas y estados de carga.
- **htmx**: Interacción SPA fluida mediante reemplazo parcial de HTML sin recargar la página.
- **Alpine.js**: Reactividad ligera para cliente, micro-animaciones y control de estados en vivo.
- **Google Material Symbols & Fonts Locales**: Iconografía served-locally sin dependencia de CDNs de internet.

---

## ✨ Funcionalidades Principales

### 1. 🎫 Gestión Completa de Tickets
- **Doble Clasificación**: Incidentes (fallos de servicio) y Solicitudes (requerimientos rutinarios).
- **Máquina de Estados Centralizada**: `NUEVO` ➔ `EN_PROCESO` ➔ `EN_ESPERA_USUARIO` / `EN_ESPERA_TERCERO` ➔ `RESUELTO` ➔ `CERRADO` / `ANULADO`.
- **Semaforización Visual de Prioridad & Estado**: Badges de color desaturados con íconos semánticos (P1 Crítica en rojo fuego, P2 Alta en naranja, P3 Media en azul, P4 Baja en gris, Resuelto en verde esmeralda).
- **Gestión Multi-rol de Estado y Prioridad**: Agentes, Solicitantes y Administradores pueden ajustar la prioridad (P1–P4) y transicionar estados de forma transparente según su criterio.

### 2. ⏱️ Reloj de SLA & Tiempo Hábil Colombiano
- **Cálculo Automático**: Mide tiempos de respuesta y resolución en minutos hábiles colombianos (descontando festivos nacionales y fines de semana).
- **Pausa Automática**: El reloj de SLA se detiene en estados de espera (`EN_ESPERA_USUARIO` / `EN_ESPERA_TERCERO`) y se reanuda al volver a proceso.
- **Edición e Inspección en Tiempo Real**: Agentes y Administradores pueden ajustar el límite de resolución con actualización instantánea al solicitante.

### 3. 💬 Hilo de Conversación Bidireccional & Notas Internas
- **Chat en Vivo**: Mensajes transmitidos al instante mediante WebSockets sin polling.
- **Burbujas Alineadas Dinámicamente**: Emisor a la derecha (fondo de acento) y Receptor a la izquierda (fondo neutro).
- **Notas Internas & `@menciones`**: Conversación privada exclusiva para el equipo técnico.
- **Gestión de Adjuntos**: Carga previa con vistas en miniatura, botón de descarte individual y limpieza automática tras el envío.

### 4. 💻 Módulo de Inventario de TI (Etapa 7)
- **Control de Activos Electrónicos**: Registro e independización de Portátiles, Computadores de Escritorio, Impresoras, Servidores y Líneas Móviles.
- **Asignación a Empleados**: Vinculación directa de equipos a personal de la empresa con historial de entregas.
- **Códigos QR & Alertas**: Generación de QR por activo y alertas inteligentes de garantías y mantenimientos preventivos.
- **Gestión Biométrica & Sincronización**: Visualización de perfiles desde IAM, aprovisionamiento y sincronización bidireccional de contraseñas (incluyendo webhook con autenticación por token seguro).

### 5. 👑 Panel de Administración Centralizado (`/admin-panel/`)
- **Control Total**: El administrador puede editar cualquier solicitud, usuario, activo o catálogo.
- **Métricas Operativas**: Tiempos de respuesta, volumen por área, cumplimiento de SLA y descargas en Excel.
- **Respaldos Automatizados**: Servicio de backup integrado en Compose (`db-backup`) para realizar volcados de base de datos de manera programada.

### 6. 👤**Módulo de Identidad y Sincronización (IAM & Fan-Out)**: 
  - **Aprovisionamiento Unificado**: Conexión automatizada y asíncrona para la gestión y reactivación de usuarios en el ecosistema GOYA (Tiquetera, Trazum, GOC, Krono y Wiki.js).
  - **Arquitectura de Sincronización Híbrida**: Propagación transaccional de credenciales (compatible con hashes `pbkdf2_sha256` de Django) mediante consultas directas a bases de datos PostgreSQL para los monolitos, y consumo automatizado vía API GraphQL para Wiki.js.
  - **Cola de Tareas Resiliente**: Sistema en segundo plano con control de estados (`PENDING`, `SUCCESS`, `FAILED`) y reintentos automáticos ante fallos de conectividad con las aplicaciones consumidoras.

  **flujo**
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
    H -->|Nueva App| W[App 5 recibe /actualización]
    
    I --> DB1[(Base de Datos GoC)]
    J --> DB2[(Base de Datos Krono)]
    K --> DB3[(Base de Datos Trazum)]
    L --> DB4[(Base de Datos Tiquetera)]
    W --> DB5[(Base de Datos App 5)]
    
    classDef default fill:#404040,stroke:#e5e5e5,stroke-width:1px,color:#ffffff
```


---

## 🚀 Cómo Ejecutar en Local

### Con Docker (Recomendado)
```bash
docker compose -f docker-compose.yml -f docker-compose.local.yml up --build
```
Queda disponible inmediatamente en `http://localhost:8084` (redirigido a través de nginx).

### Usuarios de Prueba
| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin` | Administrador Total |
| `demo.coordinador` | `demo12345` | Coordinador de TI |
| `demo.agente` | `demo12345` | Agente de Soporte |
| `demo.solicitante` | `demo12345` | Solicitante (Empleado) |

---

## 🧪 Pruebas Unitarias

```bash
docker exec tiquetera-web-1 python manage.py test
```
Suite completa con **105 tests** cubriendo arquitectura de capas, seguridad de adjuntos, máquina de estados y rutas.
