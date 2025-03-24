# Twitch About API

API sencilla para obtener la descripción ("About") de un canal de Twitch, lista para conectarse con StreamElements.

## 🚀 Despliegue en Render

1. Haz un fork o clona este repo.
2. Entra en [Render.com](https://render.com/), crea un nuevo Web Service desde tu repo.
3. Render detectará automáticamente el `render.yaml`.
4. Añade dos Environment Variables:
   - `CLIENT_ID`: Tu Client ID de Twitch.
   - `CLIENT_SECRET`: Tu Client Secret de Twitch.
5. Deploy.

## 📄 Uso

Accede:

```
https://tu-app-onrender.com/about?user=nombre_canal
```

Ejemplo para StreamElements:

```
${customapi.https://tu-app-onrender.com/about?user=${channel}}
```

## ✨ Listo para usar en el chat de Twitch!
