# ¿Cómo contribuir?

1. Instalar algún editor de código. Es recomendable [VSCode](https://code.visualstudio.com/)
2. Instalar [git](https://git-scm.com/)
3. Instalar [python](https://www.python.org/)
4. Crear una cuenta en [Github](https://github.com/)
5. Hacer un fork al repositorio.
6. Abrir una terminal y clonar el repositorio fork usando `git clone`.
7. Abrir la carpeta clonada con el editor.
8. El archivo `0.utf` es en el cual se encuentra el texto a traducir.
9. Deberás elegir cuanto vas a traducir. Por ejemplo, si actualmente la traducción se encuentra en la línea `50000` del archivo `0.utf`, podrías elegir traducir **100 líneas**.
10. Una vez traducidas las líneas que elegiste, necesitas hacer una **PR**.

## ¿Cómo hago la PR?

1. Crear una rama usando el comando `git checkout -b NOMBRE_RAMA main`. (NOMBRE_RAMA deberá seguir el formato T-FROM-TO, donde FROM y TO son la línea donde empezaste y la línea final).

Ejemplo:

```
git checkout -b T-50000-50100
```

2. Escribir `git add 0.utf`, luego `git commit -m "Translated FROM to TO"` (aquí, FROM y TO son la línea donde empezaste y la línea final). 

Ejemplo:

```
git commit -m "Translated 50000 to 50100"
```

3. Usar el comando `python percentage_calc.py TO` (aquí, TO es la línea final). Verás que aparece un número. Deberás ir al archivo `README.md` y actualizar el `Avance total` por el número que aparece.
4. Escribir `git add README.md` y luego `git commit -m "Updated percentage`.
5. Escribir `git push origin NOMBRE_RAMA`.
6. Ir a la página de Github y entrar al repositorio fork. Verás que aparece un mensaje para realizar una Pull Request. Hacer click allí.
7. Aparecerá un formulario. Rellenarlo con el siguiente formato:

```
Traducido desde 50000 hasta 50100

Avance total: 0.25/100%
```

8. Realizar la Pull Request. Deberás esperar a que sea validada. Una vez validada, deberás actualizar el repositorio fork en Github.
9. Deberás actualizar el proyecto clonado localmente. Primero usarás `git checkout main` y luego `git pull origin main`.
10. Ahora podrás repetir el proceso si quieres volver a traducir.
