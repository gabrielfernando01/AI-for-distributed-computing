![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/ai_cover.png)

## 🔧 Conocimientos de AI para computo distribuido.

### 🧠 Fundamentos prácticos:

+ Qué es un modelo supervisado / no supervisado.
+ Overfitting, regularización, validación cruzada.
+ Evaluación: accuracy, F1-score, ROC-AUC, etc.
+ Embeddings, vectores de características.
+ Transfer learning (usar modelos preentrenados).

***

## ⚙️ Herramientas y frameworks clave.

### 📌 Lo mínimo que deberías dominar:

![](https://raw.githubusercontent.com/gabrielfernando01/AI-for-distributed-computing/master/image/table_frameworks.png)

***

## 🤖 Modelos y técnicas actuales más útiles.

Aprende solo los más aplicables a procesamiento distribuido:

+ **NLP (Procesamiento de texto)**: BERT, DistilBERT, GPT (ya empaquetados).
+ **Computer Vision**: modelos ResNet, segmentación, clasificación.
+ **Recomendadores**: ALS en Spark MLlib o embeddings.
+ **Modelos de series de tiempo**: Prophet, LSTM (pero puedes integrar con Spark para escalar).

Lo clave es: saber **cómo aplicar modelos ya entrenados** sobre datos grandes.

***

## 🔌 Cómo conectar IA y Cómputo Distribuido (Scala + Spark).

Aquí una arquitectura ejemplo:

```
[1] Ingesta de datos (Kafka/S3/HDFS)
     ↓
[2] Preprocesamiento distribuido (Spark + Scala)
     ↓
[3] Aplicación de modelo (Spark MLlib o llamado a modelo HF/TF exportado)
     ↓
[4] Almacenamiento (S3 / Redshift / ElasticSearch)
     ↓
[5] Dashboard / API / MLflow monitoring
```
***

## 🎱 Types of Machine Learning:

There are many types of machine learning but the most famous types are:

+ 🥊 Supervised learning.
+ 🌟 Unsupervised learning.
+ 🔥 Reinforcement learning.

### 🥊 Supervised learning.

En el aprendizaje supervisado, el algoritmo se entrena con datos etiquetados, lo que significa que los datos de entrenamiento incluyen los pares de entrada y salida. El objetivo es aprender la correspondencia entre la entrada y la salida.

```
X -> Y 
```

Some examples of supervised learning include image classification, email spam
detection, and predicting software.

**⚡ Types of supervised learning tasks:**

1. Regression
2. Classification

**♟️ Regression**:

La regresión es un tipo de tarea de aprendizaje supervisado donde el objetivo del algoritmo es predecir una salida numérica continua o una variable objetivo. En la regresión, la salida es un número real, y el objetivo del algoritmo es aprender una correspondencia entre las características de entrada y esta salida continua.

Algunos ejemplos de tareas de regresión incluyen la predicción del precio de la vivienda, la predicción de la masa de un agujero negro, la predicción del precio de las acciones, la estimación de la edad, etc.

**🤖 Algorithms**:

+ 🍬 **Linear Regression**:

La regresión lineal es una técnica estadística y de aprendizaje automático fundamental para resolver problemas de regresión, utilizada para modelar la relación entre una variable dependiente (u objetivo) y una o más variables independientes (o características). Supone que esta relación es aproximadamente lineal, lo que significa que los cambios en las variables independientes tienen un efecto lineal sobre la variable dependiente.

- **Simple Lineal Regression**

In simple linear regression, there is only one input feature.

```
Y = wx + b
```

Y = target variable
w = pendiente
x = input feature
b = intercept

### ⭐ Overfitting

El **overfitting** (o sobreajuste) en machine learning es cuando un modelo aprende **demasiado bien los datos de entrenamiento**, incluyendo el **ruido o las particularidades** que no generalizan bien a datos nuevos. En otras palabras, el modelo **memoriza** en lugar de **aprender patrones generales**, lo que lleva a un buen rendimiento en el conjunto de entrenamiento pero **mal desempeño en datos no vistos**.

**Ejemplo sencillo**

Imagina que estás entrenando un modelo para predecir precios de casas, y una de las casas tiene un precio anormalmente alto porque es de un famoso. Si el modelo se ajusta a ese dato específico, pensará que todas las casas con características similares también deben ser carísimas, aunque eso no sea cierto.

***

**Señales de overfitting**:

+ **Baja pérdida/error en entrenamiento**, pero **alta pérdida/error en validación/test**.
+ El modelo se vuelve muy complejo: muchas capas, muchos parámetros, o árboles muy profundos (en modelos como Random Forest o XGBoost).

***

**Cómo evitar el overfiting**:

+ **Regularización**: técnicas como L1 o L2.
+ **Dropout** en redes neuronales.
+ **Reducir la complejidad** del modelo.
+ **Más datos** de entrenamiento.
+ **Validación cruzada** (cross-validation).
+ **Early stopping**: detener el entrenamiento cuando el error de validación empieza a subir

***
## 🛠️ Siguiente paso recomendado.

Construir proyecto



