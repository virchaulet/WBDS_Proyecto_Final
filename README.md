# **WBDS: Bioinformática y Ciencia de Datos**

### **¡Bienvenidxs a mi Trabajo Final de Mujeres en la Bioinformática y Ciencia de Datos!**

## **Objetivos Específicos**

1-Como mi tesis doctoral está enmarcada en el **Diseño Racional de fármacos** me propuse implementar como tema de **Bioinformática**, **Docking Molecular**.

2-Esta técnica se puede llevar a cabo mediante un Software que utiliza **comandos de Python**, por lo que podré aplicar lo visto durante el desarrollo del Camp.

3-A los **Resultados del Docking**, se los puede analizar mediante la **biblioteca Pandas** con **Google Colaboratory** y otras bibliotecas como **Seaborn, Scipy, Sklearn**, vistos también durante este Camp.

4-Para poder llevar a cabo el Docking se deben aplicar otras herramientas tanto de la Bioinformática como de la Ciencia de Datos y Lenguaje de Programación, como por ejemplo el uso de **visualizadores moleculares** (como **Chimera** o **Pymol**) y los **IDEs** o **Entornos de Desarrollo** (como **Visual Studio Code** o **Spyder**).


## **Bioinformática**
Como herramienta bioinformática a implementar, decidí hacer mi primer **Docking Molecular** aplicado al Diseño de fármacos, es decir un **acoplamiento proteína-ligando**, el cual se define como:

"El acoplamiento molecular es una técnica de **diseño de fármacos** basada en la estructura ampliamente utilizada. Utilizamos esta tecnología para **predecir las conformaciones 3D más probables de ligandos de moléculas pequeñas dentro de los sitios de unión objetivo** y para proporcionar proyecciones cuantitativas de las variaciones de energía involucradas en el evento de reconocimiento intermolecular. Además, estas estimaciones cuantitativas de la energía de unión  proporcionan clasificaciones para los compuestos acoplados, que es un parámetro útil para seleccionar ligandos para perfiles experimentales. En el diseño de fármacos, el método de acoplamiento molecular se utiliza principalmente para buscar moléculas pequeñas (hits) que tengan una buena afinidad con las moléculas diana de las bases de datos de moléculas pequeñas."

### Software utilizado para el Docking Molecular: Autodock Vina

### Requisitos del Software: son necesarios:

**1.Paquete de software ADFR:** proporciona una serie de herramientas de software para el acoplamiento automatizado y las tareas periféricas.

El paquete de software ADFR se desarrolló en el laboratorio Sanner del Centro de Biología Estructural Computacional (CCSB), anteriormente conocido como Laboratorio de Gráficos Moleculares (MGL) del Instituto de Investigación Scripps para la visualización y el análisis de estructuras moleculares. Puede encontrar más información sobre el proceso de instalación del paquete de software ADFR aquí: https://ccsb.scripps.edu/adfr/downloads . La versión actual contiene las siguientes herramientas para acoplar:

* ADFR v1.2 y scripts asociados
* AGFR v1.2
* AutoSite v1.0 y v1.1
* ADCP v1.0
* AutoGrid4.2
* preparar\_ligando
* preparar\_receptor

Además, el paquete de software ADFR proporciona una serie de herramientas de software para el acoplamiento automatizado y las tareas periféricas. Estas herramientas se implementan utilizando los lenguajes de programación Python, C++ y C y una filosofía de componentes reutilizables. Para evitar discrepancias en los paquetes de Python, optamos por cambiar la suite ADFR con un intérprete de Python autónomo que está aislado del intérprete de Python predeterminado instalado en su computadora (excepto para las instalaciones de Windows). Los detalles sobre la implementación y los paquetes proporcionados por el paquete de software ADFR se pueden encontrar aquí: https://ccsb.scripps.edu/adfr/implementation

**2\. Meeko:**

El paquete Python meeko es un nuevo tipo de paquete desarrollado en el laboratorio de Forli también en el Centro de Biología Estructural Computacional (CCSB) . Proporciona herramientas que cubren otros aspectos del acoplamiento que no maneja el paquete de software ADFR. Este paquete proporciona herramientas adicionales para los siguientes protocolos de acoplamiento:

* Atraque hidratado
* macrociclos

### Aplicación del tutorial de AutodockVina
Comencemos con nuestro primer ejemplo de acoplamiento, donde el patrón de uso típico sería acoplar una sola molécula en un receptor rígido. En este ejemplo acoplaremos el **fármaco anticanceroso** aprobado **imatinib** (Gleevec; PDB entrada 1iep ) en la estructura de **c-Abl** usando AutoDock Vina. El objetivo de este protocolo es el **dominio quinasa del protooncogén tirosina proteína quinasa c-Abl**. La proteína es un objetivo importante para la quimioterapia contra el cáncer, en particular, el tratamiento de la leucemia mielógena crónica.

#### Proteína
Si buscamos esta proteína en la base de datos **Protein Data Bank**, encontraremos el cristal de la misma, es decir que podremos conocer la estructura de la proteína de forma experimental. Luego, con esta estructura podremos realizar las técnicas computacionales que son de nuestro interés.

Si miramos en detalle, vemos que es un cristal obtenido por **Difracción de Rayos X** del dominio cinasa C-ABL en complejo con Imatinib (STI-571) cuyo PDB es **1IEP**.

Si vamos a la pestaña “3D View” de PDB  veremos la proteína en color verde junto al ligando en el **sitio de drogabilidad**.

#### Pockets
La **drogabilidad** es un concepto que describe cuán factible es que la proteína blanco se una fuertemente a un compuesto tipo droga (típicamente Kd menor a 1 μM) y que dicha unión sea biológicamente relevante, es decir, desencadene el **efecto farmacológico deseado**.

En el **diseño racional de fármacos** resulta esencial caracterizar las interacciones moleculares que puede ofrecer el blanco proteico para ser aprovechadas por moléculas pequeñas o compuestos tipo droga. La identificación de las regiones en la superficie proteica que aportan una gran contribución a la energía libre de unión proteína-ligando y, por ende, resultan cruciales para establecer dicha unión, sirve tanto para evaluar la drogabilidad de un posible  blanco como para optimizar compuestos líderes en cuanto al incremento de su afinidad>

Si buscamos más información con respecto a la **drogabilidad de esta proteína** lo podremos hacer en **CaviDB**, una base de datos en línea gratuita que provee información sobre las cavidades proteicas y sus propiedades, que permite estudiar también la diversidad conformacional de las cavidades proteicas.

Para esta proteína, encontraremos tanto la cadena A y la cadena B, en cada una de las cuales podremos estudiar sus bolsillos junto a sus características.

**Para la cadena A de la proteína:** Como vemos, la cadena A de la proteína tiene **18 cavidades**, de las cuales la cavidad 1 es la drogable, y es la de interés al momento de pensar en diseño de fármacos. Esta cavidad tiene la particularidad de ser más hidrofóbica que el resto de la superficie de la proteína, la cual interacciona con el medio en donde la misma se encuentre.

CaviDB nos brinda un gráfico en el cual podemos ver las **características de la cavidad drogable de la cadena A** como el score del pocket (bolsillo), los residuos con carga negativa, los residuos con carga positiva, el score de hidrofobicidad, etc.

Ademas, en el **grafico de “Activated residues per cavity”** vemos los residuos activados por cavidad considerando su pKa en la cadena A.

**Para la cadena B de la proteína:** Como vemos, la cadena B de la proteína tiene **21 cavidades**, de las cuales la cavidad 1 es la drogable, y es la de interés al momento de pensar en diseño de fármacos. Esta cavidad tiene la particularidad de ser más hidrofóbica que el resto de la superficie de la proteína, la cual interacciona con el medio en donde la misma se encuentre.

CaviDB nos brinda un gráfico en el cual podemos ver las **características de la cavidad drogable de la cadena B** como el score del pocket (bolsillo), los residuos con carga negativa, los residuos con carga positiva, el score de hidrofobicidad, etc.

Además en el **grafico “Activated residues per cavity”** vemos los residuos activados por cavidad considerando su pKa en la cadena B.


### Materiales para este tutorial
Considerando el tutorial brindado por AutoDockVina, se proporciona todo el material básico y se puede encontrar en el **AutoDock-Vina/example/basic\_docking/data directorio** (o en GitHub). 

Si alguna vez te sentís perdido, siempre puedes echar un vistazo a la solución aquí: **AutoDock-Vina/example/basic\_docking/solution**. 

Todos los **scripts de Python** utilizados en este tutorial (excepto prepare\_receptor y mk\_prepare\_ligand.py) se encuentran en el **AutoDock-Vina/example/autodock\_scripts** directorio, como alternativa, también podés encontrarlos en GitHub.


### Procedimiento
#### 1. Preparación del receptor/proteína

Durante este paso, crearemos un archivo PDBQT de nuestro receptor que contiene solo los átomos polares de hidrógeno y las cargas parciales. Para este paso, utilizaremos la **prepare\_receptor** herramienta de comandos de **ADFR Suite**.

Como requisitos previos:
*Un archivo de coordenadas del receptor/proteína debe contener todos los átomos de hidrógeno.

*Si está utilizando estructuras experimentales (por ejemplo, del banco de datos de proteínas ), use un editor de texto para eliminar aguas, ligandos, cofactores e iones que se consideren innecesarios para el acoplamiento.

Existen muchas herramientas para agregar los átomos de hidrógeno faltantes y la carga a una proteína, en mi caso utilicé **Chimera**, el cual es un programa de visualización que es capaz de leer un archivo pdb y generar una representación tridimensional de la macromolécula con la cual el usuario puede interactuar. Los átomos de hidrógeno y la carga se agregaron a través del siguiente proceso:

1-Cargue el PDB descargado de Protein Data Bank que contiene el ligando y la proteína junto a moléculas de agua y átomos de Cloro. (Este archivo contiene las coordenadas del receptor tomadas de la entrada 1iep del PDB )

2-Seleccione las moléculas de agua, átomos de Cloro y el ligando y los elimine.

3-Adicione átomos de hidrógeno y carga:

i) **Tools → Structure Editing → AddH → OK.**  Dado que el archivo de ligandos no incluye los átomos de hidrógeno, los agregaremos.

ii) **Tools → Structure Editing → AddCharges → Gasteiger → OK.**

4-Guarde el **PDB de la proteína**, no la sesión.

Luego procedemos a transformar el archivo de la proteína de un **PDB** a un **PDBQT** mediante:
**$ ubicacion/prepare\_receptor -r 1iep\_receptorH.pdb -o 1iep\_receptor.pdbqt**

En mi computadora:
(base) virginia@virginia-IdeaPad-3-15ITL6:~/Escritorio/Doctorado/LideB/Docking/Tutorial/Archivos$ /home/virginia/ADFRsuite-1.0/bin/prepare\_receptor -r 1iep\_conH.pdb -o 1iep\_conH\_final.pdbqt

adding gasteiger charges to peptide

Nos devuelve **en la carpeta donde estamos trabajando** el pdb, un archivo del **receptor en formato pdbqt**.


#### 2. Preparación del ligando

Este paso es muy similar al paso anterior. También crearemos un archivo PDBQT a partir de un archivo de molécula de ligando (en formato MOL/MOL2 o SDF) utilizando el **Meeko paquete python**.

Como requisitos previos:
*Un archivo de coordenadas del ligando debe contener todos los átomos de hidrógeno.

*Si está utilizando estructuras experimentales (por ejemplo, del banco de datos de proteínas ), use un editor de texto para eliminar aguas, proteínas, cofactores e iones que se consideren innecesarios para el acoplamiento.

Existen muchas herramientas para agregar los átomos de hidrógeno faltantes y la carga al ligando, en mi caso utilicé **Chimera**, el cual es un programa de visualización que es capaz de leer un archivo pdb y generar una representación tridimensional de la molécula con la cual el usuario puede interactuar. Los átomos de hidrógeno y la carga se agregaron a través del siguiente proceso:

1-Cargue el PDB descargado de Protein Data Bank que contiene el ligando y la proteína junto a moléculas de agua y átomos de Cloro.

2-Seleccione las moléculas de agua, átomos de Cloro y la proteína y elimine.

3-Adicione átomos de hidrógeno y carga:

i) **Tools → Structure Editing → AddH → OK.**  Dado que el archivo de ligandos no incluye los átomos de hidrógeno, los agregaremos.

ii) **Tools → Structure Editing → AddCharges → Gasteiger → OK.**

4-Guarde el **MOL2 de ligando**, no la sesión.

Luego procedemos a transformar el archivo del ligando de un **MOL2** a un **PDBQT** mediante:
**$ ubicacion/mk\_prepare\_ligand.py -i 1iep\_ligand.sdf -o 1iep\_ligand.pdbqt**

En mi computadora:
(base) virginia@virginia-IdeaPad-3-15ITL6:~/Escritorio/Doctorado/LideB/Docking/Tutorial/Archivos$ /home/virginia/ADFRsuite-1.0/bin/prepare\_ligand -i Ligando1.mol2 -o LIG.pdbqt

Para mayor comodidad, el tutorial de AutoDock Vina proporciona el archivo (ver data directorio): **1iep\_ligand.sdf** 


#### 3.Caja de Docking
Para poder Dockear, debemos determinar la ubicación y el tamaño de la caja del Docking\. Para realizar esto recurrimos a la **inspección visual del Ligando en la Proteína de estudio** mediante un visualizador como **Chimera o Pymol**\.

En mi caso utilicé el visualizador Chimera para poder definir ambos parámetros:

**1-Ubicación = Center [x, y, z]**

Para mirar las coordenadas hay dos opciones:

i-Desde el Ligando: te centras en el Ligando y clickeas

ii-Desde el Blanco: desde el blanco seleccionas un aminoacido el cual sea mas probable que interaccione por la visualización.


Una vez elegida la forma de proceder, para ver las coordenadas recurriremos a:

**Tools→Surface/BindingAnalysis → AutoDock Vina.**


**2-Tamaño = Box\_size [n, n, n]**

Se clickea en **Resize search volumen** using “cambiar el tamaño del volumen de búsqueda usando” button x (tenes opciones para elegir diferentes botones)

Cambio el tamaño de la caja, en mi caso se disminuyó de tamaño


#### 4.Script
Una vez obtenidos los archivos PDBQT del receptor y el ligando, y los parámetros de la caja del Docking, es momento de armar el **script para Dockear** con script en lenguaje **Python**, utilizando el editor de código **Visual Studio Code**\.

**Python\_ Script\_AutoDockVINA\_WBDS\_final**

En este **script** deberemos setear:
- **Archivos** en formato **pdbqt** de **ligando** y **receptor** con su respectiva ubicación.
- **Parámetros** obtenidos anteriormente para la **caja de docking** (ubicación y tamaño)
- Indicarle el **número de poses** a obtener del **ligando**
- La **exhaustividad** con la que se trabajará, es decir  la cantidad de esfuerzo computacional utilizado durante un experimento de acoplamiento. El valor de exhaustividad predeterminado es 8, pero al aumentarlo dará un resultado de acoplamiento más consistente. Es por eso que al aumentar la exhaustividad, podemos pedirle menos poses del ligando, ya que nos devolverá las poses más confiables.
- El **campo de fuerza**
- También debemos crear los **archivos.txt** de el **output\_file**  y el **readme\_file** indicando su ubicación.

Nota: Para este archivo.py se usaron los script de open access dados por el tutorial de Autodock Vina para Dockear.


#### 5. Corrida del Docking
Abro una **terminal** de Linux y en la misma llamo a **Python\_ Script\_AutoDockVINA\_WBDS\_final** y lo ejecuto\.


## **Ciencia de Datos**
#### 1. Análisis de Resultados: Pandas
Una vez corrido el Docking, debemos analizar los datos del output y del archivo de Resultados, para lo cual utilicé un **Cuaderno de Google** y a la **librería Pandas**\.

Los archivos de salida son:

**output\_file.txt = Ligando,TOP SCORE**

**LIG.pdbqt**,-13.16

**Resultados\_LIG.pdbqt**= Nos devuelve 8 modelos, debido a que de las 10 poses seteadas, el algoritmo solo puede resolver 8.

Nota: este Cuaderno de Google está subido como archivo "**Cuaderno_Trabajo_Final_Docking.ipynb**"

Para realizar el análisis, se puede abrir un Cuaderno de Google y crear un **DataFrame** con los Scores obtenidos para cada conformación de ligando luego del Docking.

#### 2. Análisis de Resultados: scipy, seaborn, sklearn
Luego de obtener curva Score vs Modelos, quise estudiar si existe correlación entre los Modelos y el Score obtenido luego del Docking, y en caso de que exista, quise estudiar si se aproxima a una correlación lineal.

Para esto se aplicaron las bibliotecas:

🔢 **scipy:** una biblioteca de algoritmos matemáticos, muy útiles en el campo de la ciencia de datos;

📈 **seaborn, matplotlib:** herramientas de graficación que complementan y extienden a las operaciones .plot provistas por pandas;

🤖 **sklearn (abreviatura de scikit-learn):** una popular biblioteca con algoritmos de aprendizaje automático, entre los cuales se encuentra, obviamente, soporte para regresión lineal 🎊

**¿Cuáles de estas variables están relacionadas?** 😛

i)Para responder esta pregunta, una buena primera forma de aproximarse es generar una **matriz de correlación**, que nos dirá el grado en que los cambios de cualquiera de las variables acompañan los cambios de cualquiera de las otras ↔️.

Para ello, los DataFrames cuentan con la operación corr:

**correlaciones = df.corr()**

**correlaciones**

Esta matriz mostrará, por cada par de variables, cuán relacionadas están en una **escala de -1 a 1**, siendo:

**1:** altamente correlacionadas y directamente proporcionales. ↗️ Si una variable crece, la otra también;

**0:** sin ningún tipo de correlación. 🤷 Los cambios en una no parecen influir en la otra;

**-1:** altamente correlacionadas e inversamente proporcionales. ↘️ Si una variable crece, la otra decrece.


**correlaciones['Score']**

En términos absolutos, la correlación entre estas dos variables es mayor a 0.5 y además la correlación es de signo positivo, lo que indica una relación directa.

Para nuestro caso vemos que la **correlación entre Modelo y Score es de 0.84, por lo que vemos que está correlacionada.**



ii)Otra forma útil de visualizar estas correlaciones es mediante un **mapa de calor** 🥵, que asigne puntos más claros a aquellos pares con mayor correlación:

**sns.heatmap(correlaciones.abs())**

Para nuestro caso **Todo parece indicar que existe un vínculo entre el Modelo y el Score de este lote de datos.** 


Con esto en mente, ya podemos intentar expresar este vínculo como **Score = f(Modelo)**, siendo f una función lineal, ¿no? 😀

Bueno, si bien tenemos elementos para explorar esa posibilidad, no nos apresuremos 🐢. **La relación podría aún no ser lineal, o incluso podría no ser significativa y deberse a, lisa y llanamente, la casualidad.**

Por eso, se harán algunas pruebas más.

i)📈 Primero, graficaremos las observaciones empleando un **regplot**, que combina un gráfico de dispersión y superpone los resultados sobre una recta ideal de regresión:

**sns.regplot(x="Modelo", y="Score", data=df)**

Y luego calcularemos: **Coeficiente de correlación de Pearson** y su **valor P**

**Coeficiente de correlación de Pearson:** una medida de co-variación entre las variables, tal que valores absolutos cercanos a 1 indican alta correlación, mientras que los cercanos a 0 indican correlación baja;

**Valor P:** es una medida de confianza que nos dirá cuán probable es que los resultados sean producto de la casualidad. Cuanto más cercana a cero, menos probable es que el resultado sea producto del azar. En la práctica se suele considerar **no significativo** a cualquier resultado con **pvalue** por encima de **0.05** (o 0.01, si se busca más rigor), es decir que será **significativo** aquel cuyo **p-valor < 0.05**.

**corr, pvalue = pearsonr(x = df['Modelo'], y = df['Score'])**

**print("Coeficiente de correlación de Pearson:", corr)**

**print("P-value:", pvalue)**

Para nuestro caso:

Coeficiente de correlación de Pearson: 0.8448507044302611

P-value: 0.008283899402752945

El **p-valor es cercano a cero**, siendo el resultado **significativo** e indicando que no es producto del azar y el **valor de pearson coincide con el obtenido mediante corr()** debido a que corr() utiliza por defecto el método de Pearson ('pearson'). 


ii)Ahora que validamos gráfica y numéricamente que la correlación es significativa (aunque medianamente fuerte ≈ 0.84), podemos finalmente desarrollar (o como se suele decir frecuentemente, **ajustar**) nuestro modelo de **regresión lineal simple**.

💺 **Ajustar al modelo consiste en estimar**, a partir de los datos disponibles:

-la recta que **minimice la distancia ε** entre las observaciones de x y ésta;

-encontrar los **valores de los coeficientes de regresión** que maximizan la probabilidad de que la recta prediga los valores observados.



El método más utilizado para ésto es el de **mínimos cuadrados ordinarios** (o OLS, por sus siglas en inglés) y **scikit-learn** lo implementa mediante LinearRegression():

**X = df[['Modelo']]**

**y = df['Score']**

**modelo = LinearRegression()**

**modelo.fit(X = X.values, y = y)**

**LinearRegression**

**LinearRegression()**


Luego debemos crear un modelo y seguidamente ajustarlo utilizando su operación **fit**, indicando los valores de X e y.

Luego podremos imprimir los valores encontrados de **ordenada al origen** (intercept\_) y la **pendiente** (el primer valor del vector coef\_):

**print("Ordenada:", modelo.intercept\_)**

**print("Pendiente:", list(zip(X.columns, modelo.coef\_.flatten())))**

Para nuestro caso:

Ordenada: -12.827

Pendiente: [('Modelo', 0.3806666666666668)]


Por un lado pudimos establecer que existe un **vínculo entre ambas variables (corr ≈ 0.84)** y que dicho vínculo **no parece el mero producto del azar (pvalue ≪ 0.05)**, y por otro pudimos aproximarlo a una recta, pero **aún estamos lejos de haber evaluado completamente al modelo.** 🙃


**Aún hay muchas cosas que no sabemos!** Por ejemplo: **¿cuán bueno es el modelo? ¿Los datos caen efectivamente en la recta?**


Una primera aproximación a las preguntas es utilizar la **métrica R2**, que nos indica cuán bueno es el ajuste del modelo.

Esta medida estadística oscila entre:

**0**:los datos predicho no se ajustan a las observaciones

**1**:los datos predichos se ajustan perfectamente a las observaciones.

La operación score de nuestro modelo nos retornará justamente esta métrica (que dicho sea de paso, en los modelos de regresión lineal simple su valor se corresponde con el cuadrado de la correlación de Pearson 💡):

**print("Coeficiente de determinación R²:", modelo.score(X.values, y))**

Para nuestro caso:

Coeficiente de determinación R²: 0.7137727127763094

Como vemos, el **R² arrojó un valor más bien medio (≈ 0.71), lo que nos indica que el modelo es medianamente bueno**. Eso no significa necesariamente que el modelo sea inválido, sino que la relación lineal encontrada explica de bastante completo a la variable y, aunque podría ser mejor su correlación.


## Conclusión

De acuerdo a los objetivos propuestos y lo realizado durante este trabajo, puedo concluir que pude realizar mi primer **Docking Molecular**, obteniendo las estructuras de la **proteína** y **ligando** de **Protein Data Bank**. Este docking pudo hacerse siguiendo un **tutorial brindado por AutoDockVina**, el cual contiene scripts en lenguaje de Python, pudiendo implementar lo aprendido durante el Camp.

Luego los resultados obtenidos del Docking pudieron ser analizados por herramientas vistas, como fue el uso de la **biblioteca de Pandas**, y sus respectivas funciones. Además se pudo recurrir a herramientas estadísticas como es la correlación de datos, y si los mismos ajustan a una regresión lineal.

Finalmente, concluímos que **la pose 1 del ligando fue la de mejor Score**, es decir la pose de ligando que resultó con la **interacción más estable con la proteína** (valor más negativo de Score frente al resto de los valores). Además pudimos ver que los Scores se correlacionan con las poses de los ligandos y se ajustan a un modelo lineal.


## Bibliografía

https://drug-discovery.creative-biostructure.com/molecular-docking-p39?gclid=CjwKCAjw_MqgBhAGEiwAnYOAevOfGSp5WSJB4Tyr0Arb2EnLM3ZAFGmpo2eS1pdeIy747onbp4UXBBoCyW8QAvD_BwE

https://www.rcsb.org/structure/1iep

https://www.cavidb.org/chains/6290f658d58b5cfe1dd4c12a?q=1IEP

https://bibliotecadigital.exactas.uba.ar/download/tesis/tesis_n6457_Arcon.pdf

https://autodock-vina.readthedocs.io/en/latest/docking_python.html
