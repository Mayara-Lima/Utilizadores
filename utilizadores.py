
# Fazer um programa que cumpra as seguintes instruções:
# Criar um conjunto chamado utilizadores com os utilizadores Marta, David, Elvira, Juan e Marcos;
# Criar um conjunto chamado administradores com os administradores Juan e Marta;
# Apagar o administrador Juan do conjunto de administradores;
# Adicionar Marcos como um novo administrador, mas não o apagar do conjunto de utilizadores;
# Imprimir todos os utilizadores e devidas informações por ecrã.


usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.discard("Juan")
administradores.add("Marcos")
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "É administrador")
    else: print(usuario)