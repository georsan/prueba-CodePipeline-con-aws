# Sam y Github actions

Para integrar Sam y  Github actions se tienen que seguir los siguientes pasos:

 - Crear un proyecto sam
 - Crear bucket s3 sin ACL (esto se tiene que hacer manual debido a que con cli genera error)
 - Configurar un pipeline para ello se utiliza el comando **sam pipeline bootstrap** yse siguen los pasos,en una parte la cli pide el ARN del bucket de s3
 - Luego de que se haya configurado la cli genera un usuario iam con este usuario lo debemos colocar en el apartado de **Actions secrets and variables** que se encuentra en la settings del repositorio de github.
 - luego hacer push desde el entorno local.


