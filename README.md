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

## 🤖 3. Modelos y técnicas actuales más útiles.

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

## 🛠️ Siguiente paso recomendado.

Construir proyecto



