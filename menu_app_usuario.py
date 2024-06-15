from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None

while opcion != 5:
    print('Opciones: ')
    print('1.- Listar ususarios')
    print('2.- Agregar usuario')
    print('3.- Modificar usuario')
    print('4.- Eliminar usuario')
    print('5.- Salir')
    opcion = int(input('Escribe la opción del 1 al 5: \n'))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username. \n')
        password_var = input('Escribe el password: \n')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuaros insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Ecribe el id_usuario a modificar: \n'))
        username_var = input('Escribe el nuevo username: \n')
        password_var = input('Escribe el nuevo password: \n')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados} \n')
    elif opcion == 4:
        id_usuario_var = int(input('Ecribe el id_usuario a eliminar: \n'))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados} \n')

else:
    log.info('Salimos de la aplicación...')