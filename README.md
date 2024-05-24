Descripción:
Este programa implementa un sistema básico de CRM utilizando Python y Django. 
El programa permite realizar las operaciones básicas de CRUD sobre datos de clientes. 
El desarrollo se ha realizado utilizando vistas basadas en funciones.

Tecnologías utilizadas:
Lenguaje: Python
Framework web: Django
Base de datos: MySQL
Libreria: Bootstrap

Caso de Uso 1: Registro de un nuevo usuario
- Registro de un nuevo usuario
Actor:
Nuevo usuario
Objetivo:
Permitir a un nuevo usuario registrarse en el sistema CRM.

-Escenario Principal:

El usuario accede a la página de registro (/register).
El usuario introduce sus datos (nombre de usuario, contraseña, etc.) en el formulario de registro.
El usuario hace clic en "Registrarse".
El sistema valida los datos ingresados y guarda la nueva cuenta de usuario.
El sistema autentica automáticamente al usuario y lo inicia sesión.
El sistema redirige al usuario a la página de inicio (/home) con un mensaje de éxito.

-Escenarios Alternativos:
A1: Si el formulario contiene datos inválidos:
El sistema muestra un mensaje de error indicando los problemas específicos.
El usuario corrige los errores y vuelve a enviar el formulario.

-Precondiciones:
-El usuario no debe tener una cuenta registrada en el sistema.

-Postcondiciones:
El nuevo usuario tiene una cuenta creada y está autenticado en el sistema.

-Excepciones:
E1: Error de conexión a la base de datos durante el registro:
El sistema muestra un mensaje de error indicando que no se pudo completar el registro debido a problemas técnicos.
El usuario puede intentar registrarse nuevamente más tarde.

------------------------------------

Caso de Uso 2: Añadir un nuevo registro
-Añadir un nuevo registro

Actor:
Usuario autenticado
Objetivo:
Permitir al usuario autenticado añadir un nuevo registro de persona en el sistema CRM.

-Escenario Principal:

El usuario autenticado accede a la página de añadir registro (/add_record).
El usuario introduce los datos de la nueva persona en el formulario.
El usuario hace clic en "Guardar".
El sistema valida los datos ingresados y guarda el nuevo registro en la base de datos.
El sistema redirige al usuario a la página de inicio (/home) con un mensaje de éxito.

-Escenarios Alternativos:
A1: Si el usuario no está autenticado:
El sistema redirige al usuario a la página de inicio de sesión (/home) con un mensaje indicando que debe iniciar sesión.

-Precondiciones:
El usuario debe estar autenticado en el sistema.

-Postcondiciones:
El nuevo registro de persona se guarda en la base de datos y se muestra en la lista de registros.

-Excepciones:
E1: Si el formulario contiene datos inválidos:
El sistema muestra un mensaje de error indicando los problemas específicos.
El usuario corrige los errores y vuelve a enviar el formulario
