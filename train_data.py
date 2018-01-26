#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, print_function



TRAIN_DATA = [
    ("Muy buena hierba", {
        'entities': [(10, 16, 'DRUG')]
    }),

    ("Buenas tardes Jose", {
        'entities': [(14,18,'PER')]
    }),

    ("Linda maria me fume en Roma", {
        'entities': [(6, 11, 'DRUG'), (23,27,'LOC')]
    }),

    ("Google tiene una oficina en Buenos Aires", {
        'entities': [(0,6,'ORG'),(28,40,'LOC')]
    }),

    ("Jose fue a la escuela a las 8am", {
        'entities': [(0, 4, 'PER'),(14,21,'MISC')]
    }),

    ("¿Cuanto la marihuana?", {
        'entities': [(11, 20, 'DRUG')]
    }),

    ("alto faso el de Jose", {
        'entities': [(5, 9, 'DRUG'),(16,20,'PER')]
    }),

    ("weed se la llama internacionalmente", {
        'entities': [(0, 4, 'DRUG')]
    }),

    ("ganya para todos!, aclamaron con un grito", {
        'entities': [(0, 5, 'DRUG')]
    }),

    ("Hachís o polen, como quieras decirle, tambien chocolate. Todas estas palabras son utilizadas", {
        'entities': [(0, 6, 'DRUG'),(9, 14, 'DRUG'),(46, 55, 'DRUG')]
    }),
    
    ("Distintas formas de llamar al porro: por ejemplo, canuto, purito, cañon, fino, faso o un puro", {
        'entities': [(30, 35, 'DRUG'),(50, 56, 'DRUG'),(58, 64, 'DRUG'), (66, 71, 'DRUG'),(73, 77, 'DRUG'),(79, 83, 'DRUG'),(89, 93, 'DRUG')]
    }),
    
    ("A la cocaína, también conocida como 'merca', le dicen 'la porquería', 'falopa', 'cameruza' o 'camer'.", {
        'entities': [(5, 12, 'DRUG'),(37, 42, 'DRUG'),(55, 67, 'DRUG'),(71, 77, 'DRUG'),(81, 88, 'DRUG'),(93, 98, 'DRUG')]
    }),
    
    ("La pasta base es el deshecho de la  cocaína y también se la llama 'paco'. En la jerga, los dealers denominan a cada dosis de cocaína como 'camisa' y a la dosis de paco 'pantalón'", {
        'entities': [(3, 13, 'DRUG'),(36, 43, 'DRUG'),(67, 71, 'DRUG'), (66, 71, 'DRUG'),(125, 132, 'DRUG'),(139, 145, 'DRUG'),(163, 167, 'DRUG'), (169, 177, 'DRUG')]
    }),
    
    ("Vendiendo merca en la plaza me hice rico", {
        'entities': [(10, 15, 'DRUG'), (22,27,'LOC')]
    }),

    ("Android tiene una aplicación que permite validar archivos", {
        'entities': [(0, 7, 'MISC')]
    }),

    ("aguante el paco estaba escrito en el mural del parque, en frente a Carrefour", {
        'entities': [(11, 15, 'DRUG'),(47,53,'LOC'),(67,76,'ORG')]
    }),

    ("Fueron secuestradas 4 toneladas de cocaina en Mendoza", {
        'entities': [(35, 42, 'DRUG'),(46, 53, 'LOC')]
    }),
    
    ("Gustavo viaja a China dentro de un mes para ver el nuevo prototipo de autos electricos", {
        'entities': [(0, 7, 'PER'),(16, 21, 'LOC')]
    }),
    
    ("La code, o codeina se popularizó gracias a la nueva tendencia musical", {
        'entities': [(3, 7, 'DRUG'),(11, 18, 'DRUG')]
    }),
    
    ("Linda tarde para ir de visita al museo de Mar del Plata", {
        'entities': [(33, 38, 'LOC'),(42, 55, 'LOC')]
    }),
    
    ("Maria compra Coca-Cola en el camino", {
        'entities': [(0, 5, 'PER'),(13, 22,'MISC')]
    }),

    ("Buenas tardes Raul", {
        'entities': [(14,18,'PER')]
    }),

    ("Acaba de decir que se fumó un cañon", {
        'entities': [(30, 35, 'DRUG')]
    }),

    ("Gastón no va a terminar de escribir esto nunca?", {
        'entities': [(0, 6, 'PER')]
    }),

    ("El nuevo Ford Focus dicen que funciona muy bien", {
        'entities': [(9, 13, 'ORG'), (14, 19, 'MISC')]
    }),

    ("Florencia quiere ir a la playa, pero Manu no la deja", {
        'entities': [(0, 9, 'PER'),(25, 30, 'LOC'),(37, 41, 'PER')]
    }),

    ("Avisame a que hora vas al banco x que haora no estoi en casa asi yo voy para casa y te acompaño yegua", {
        'entities': [(32, 33, 'ME'),(38, 43,'ME'),(47, 52, 'ME'),(56, 60, 'MISC'),(77, 81, 'MISC')]
    }),

    ("Gordi mañana te alcansa la plata la maga x que yo no voy a estar besos mi amor", {
        'entities': [(16, 23, 'ME'),(36, 40, 'PER'), (41, 42, 'ME')]
    }),

    ("Bien amiga aca estoy en neco tomandoo un vinito con jose caceres jaaa", {
        'entities': [(24, 28, 'ME'),(29, 37, 'ME'),(41, 47, 'DRUG'),(52, 64, 'PER'),(65, 69, 'ME')]
    }),

    ("No ay ninguna amiga para el cabezita jaaaaaa", {
        'entities': [(3, 5, 'ME'),(28, 36, 'ME'),(37, 44, 'ME')]
    }),

    ("aaaaa es de balcarceeeee", {
        'entities': [(0, 5, 'ME'),(12, 20, 'LOC'), (12, 24, 'ME')]
    }),

    ("Hola ma estas en tu kasa", {
        'entities': [(5, 7, 'ME'),(20, 24, 'ME')]
    }),
    
    ("Si iria pero sola no da si a magali no la dejan entrar", {
        'entities': [(29, 35, 'PER')]
    }),
    
    ("Tengo un puro excelente", {
        'entities': [(9, 13, 'DRUG')]
    }),
    
    ("En Youtube hay videos de lo que gustes", {
        'entities': [(3, 10, 'MISC')]
    }),
    
    ("SpaCy debe entrenarse para poder detectar las drogas", {
        'entities': [(0, 5, 'MISC'),(46, 52, 'DRUG')]
    }),

    ("Carlos tiene una chala tatuada", {
        'entities': [(0, 6, 'PER'), (17, 23, 'DRUG')]
    }),

    ("Audi es de Alemania", {
        'entities': [(0,4,'ORG'),(11, 19, 'LOC')]
    }),

    ("Lindo canuto me fume en el bosque", {
        'entities': [(6, 12, 'DRUG'), (27,33,'LOC')]
    }),

    ("Fasta cierra a las 3pm", {
        'entities': [(0, 5, 'ORG')]
    }),

    ("Fumando weed todo el dia, asi dice la canción", {
        'entities': [(8, 12, 'DRUG')]
    }),

    ("Holanda posee en su bandera los colores azul, blanco y rojo", {
        'entities': [(0, 7, 'LOC')]
    }),

    ("Cuando hablamos de hierba nos referimos a droga en este contexto", {
        'entities': [(19, 25, 'DRUG'),(42, 47, 'DRUG')]
    }),
    
    ("La casa de Olivia queda a la vuelta de la mia", {
        'entities': [(3, 7, 'LOC'),(11, 17, 'PER')]
    }),
    
    ("Google posee una aplicación para android que permite localizar los mejores lugares turisticos", {
        'entities': [(0, 6, 'ORG'),(33, 4, 'MISC')]
    }),
    
    ("Hablemos de comprar cameruza", {
        'entities': [(20, 28, 'DRUG')]
    }),

    ("Incendiaron una plantación de marihuana en Misiones", {
        'entities': [(30, 39, 'DRUG'),(43, 51, 'LOC')]
    }),

    ("Estados Unidos tiene como presidente a Donald Trump", {
        'entities': [(0,14,'LOC'),(39, 51, 'PER')]
    }),

    ("Te llevo una ensalada", {
        'entities': [(13, 21, 'DRUG')]
    }),

    ("un gramo pa' la peda", {
        'entities': [(3, 8, 'DRUG'),(16, 20, 'DRUG')]
    }),

    ("Iremos al baile", {
        'entities': [(10, 15, 'MISC')]
    }),

    ("Marcha a favor de la legalización de la marihuana", {
        'entities': [(0, 49, 'MISC'),(40, 49, 'DRUG')]
    }),

    ("Jose Lopez fue el primero en entrar a la iglesia", {
        'entities': [(0, 10, 'PER'),(41, 48, 'MISC')]
    }),
    
    ("En Octubre sale un nuevo juego de Konami para la PlayStation 4", {
        'entities': [(34, 40, 'ORG'),(49, 62, 'MISC')]
    }),
    
    ("Gabriel es adicto a la cocaina", {
        'entities': [(0, 7, 'PER'),(23, 30, 'DRUG')]
    }),
    
    ("mreca .. escribo mal la palabra ", {
        'entities': [(0, 5, 'DRUG')]
    }),

    ("El festival de cine se hace en Mar del Plata", {
        'entities': [(3, 19, 'MISC'),(31, 44, 'LOC')]
    }),

    ("Me gustaria entrenar, pero debo seguir escribiendo oraciones para SpaCy", {
        'entities': [(68,74,'MISC')]
    }),

    ("Maria se fumo una maria, muy gracioso lo de Maria", {
        'entities': [(0, 5, 'PER'), (18,23,'DRUG'), (44, 49, 'PER')]
    }),

    ("Entre la lista de drogas estimulantes están:", {
        'entities': [(18, 24, 'DRUG')]
    }),

    ("Éxtasis también llamado pepas", {
        'entities': [(0, 7, 'DRUG'), (24, 29, 'DRUG'), (24, 28, 'DRUG')]
    }),

    ("Sustancias de tipo anfetaminico (anfetamínico), asi cubro ambas ", {
        'entities': [(0, 10, 'DRUG'), (19, 31, 'DRUG'), (33, 45, 'DRUG')]
    }),

    ("Como la efedrina o la pseudoefedrina", {
        'entities': [(8, 16, 'DRUG'),(22, 36, 'DRUG')]
    }),
    
    ("Se decia que Jonathan tomaba esteroides", {
        'entities': [(13, 21, 'PER'),(29, 39, 'DRUG')]
    }),
    
    ("rivotril triene efecto depresor.", {
        'entities': [(0, 8, 'DRUG')]
    }),
    
    ("La pasta base es el deshecho de la  cocaína y también se la llama 'paco'. En la jerga, los dealers denominan a cada dosis de cocaína como 'camisa' y a la dosis de paco 'pantalón'", {
        'entities': [(3, 13, 'DRUG'),(36, 43, 'DRUG'),(67, 71, 'DRUG'), (66, 71, 'DRUG'),(125, 132, 'DRUG'),(139, 145, 'DRUG'),(163, 167, 'DRUG'), (169, 177, 'DRUG')]
    }),

    ("el xanax y el valium tambien son depresores", {
        'entities': [(3, 8, 'DRUG'), (14, 20, 'DRUG')]
    }),

    ("popper, ladys, dick, boxer (gale, galuche, sacol) son inhalables", {
        'entities': [(0, 6, 'DRUG'),(8, 13, 'DRUG'),(15, 19, 'DRUG'), (21, 26, 'DRUG'),(28, 32, 'DRUG'),(34, 41, 'DRUG'),(43, 48, 'DRUG')]
    }),

    ("morfina, heroina, codeina, metadone y el opio son narcoticos (narcóticos)", {
        'entities': [(0, 7, 'DRUG'),(9, 16, 'DRUG'),(18, 25, 'DRUG'), (27, 35, 'DRUG'),(41, 45, 'DRUG'),(50, 60, 'DRUG'),(62, 72, 'DRUG')]
    }),

    ("Alucinógenos: LSD (tripis, acidos)", {
        'entities': [(0, 12, 'DRUG'),(14 , 17, 'DRUG'),(19 , 25, 'DRUG'),(27 , 33, 'DRUG')]
    }),

    ("En Irlanda consumen mucha ketamina (keta, k, ketacet entre otros) ", {
        'entities': [(0, 7, 'MISC'),(23, 31, 'DRUG'),(33, 37, 'DRUG'), (39, 40, 'DRUG'),(42, 49, 'DRUG')]
    }),

    ("Lautaro vendia GHB en la escuela", {
        'entities': [(0, 7, 'PER'),(15, 18, 'DRUG'),(25, 32, 'DRUG')]
    }),

    ("Jorge esta yendo a Polonia de vacaciones", {
        'entities': [(0, 5, 'PER'),(19, 26, 'MISC')]
    }),
    
    ("Ines Montani recomienda entrenar con minimo 100 oraciones", {
        'entities': [(0, 12, 'PER')]
    }),
    
    ("Dejemos de lado la falopa y escribamos sobre la playa de Corea del Sur", {
        'entities': [(19, 25, 'DRUG'),(48, 53, 'MISC'),(57, 70, 'MISC')]
    }),
    
    ("Ramiro y Guido saben que soy el mejor jugando", {
        'entities': [(0, 6, 'PER'),(9, 14, 'PER')]
    }),

    ("Facebook, Google, Amazon, y Microsoft son organizaciones", {
        'entities': [(0, 8, 'ORG'),(10, 16, 'ORG'),(18, 24, 'ORG'),(28, 37, 'ORG')]
    }),

    ("El dealer que solo tenia hachis", {
        'entities': [(25,31,'DRUG')]
    }),

    ("Emiliano fue al Tomorrowland", {
        'entities': [(0, 8, 'PER'), (16,28,'MISC')]
    }),

    ("De Alemania, de Croacia, de Brasil. Habie gente de todos lados!", {
        'entities': [(3, 11, 'LOC'),(16, 23, 'LOC'),(28, 34, 'LOC')]
    }),

    ("Que no pare la fiesta", {
        'entities': [(15, 21, 'MISC')]
    }),

    ("Esto no aporta en nada, solo en randomizar", {
        'entities': []
    }),

    ("Y la otra mitad la dividio para la moni y romina", {
        'entities': [(35, 39, 'PER'),(42, 48, 'PER')]
    }),
    
    ("En casa pero no entre a la comisaria y tuve que llamar a la madre que estava llendo para alla", {
        'entities': [(3, 7, 'MISC'),(27, 36, 'MISC'),(70, 76, 'ME'),(77, 83, 'ME')]
    }),

    ("Jaja. Buen kuando la veas avisale. Td bien x ai?", {
        'entities': [(0, 5, 'ME'),(11, 17, 'ME'),(35, 37, 'ME'),(43, 44, 'ME'),(45, 47, 'ME')]
    }),

    ("Besos cuidensen", {
        'entities': [(6, 15, 'ME')]
    }),

    ("Estoi con la abuela llamala a  mi cel ahora", {
        'entities': [(0, 5, 'ME'),(34, 37, 'ME')]
    }),

    ("Pone la pava, estoy esperando al camion", {
        'entities': []
    }),

    ("8 años de carcel para Fausto por la venta de sustancias", {
        'entities': [(22, 28, 'PER'),(45, 55, 'DRUG')]
    }),
    
    ("Me gustaria tener un texto con todos los datos juntos", {
        'entities': []
    }),
    
    ("en Rio de Janeiro se consume mucha merca, especialmente en las favelas", {
        'entities': [(3, 17, 'LOC'),(35, 40, 'DRUG'),(63, 70, 'MISC')]
    }),
    
    ("Gaston y Gerardo se quedan en Fasta hasta las 3pm", {
        'entities': [(0, 6, 'DRUG'),(9, 16, 'DRUG'),(30, 35, 'ORG')]
    }),

    ("Solamente quedan 20 oraciones", {
        'entities': []
    }),

    ("Le dieron 20 gramos de cocaina", {
        'entities': [(23,30,'DRUG')]
    }),

    ("Linda maria se fumo el Jony", {
        'entities': [(6, 11, 'DRUG'), (23,27,'PER')]
    }),

    ("¿Cuanto la caminsa?", {
        'entities': [(11, 18, 'DRUG')]
    }),

    ("pepa se le dice al LSD", {
        'entities': [(0, 4, 'DRUG'),(19, 22, 'DRUG')]
    }),

    ("zona ganya es una banda de chile", {
        'entities': [(5, 10, 'DRUG'), (27, 32, 'LOC')]
    }),

    ("vamos a escribir todo mal, por ejemplo: kiero kokaina", {
        'entities': [(46, 53, 'DRUG')]
    }),
    
    ("Bruno nos va a traer las conversaciones", {
        'entities': [(0, 5, 'PER')]
    }),
    
    ("Me tengo que ir a mi casa", {
        'entities': [(21, 25, 'MISC')]
    }),
    
    ("Me siento por las nubes", {
        'entities': []
    }),

    ("Vendian porro en la plaza San Martin", {
        'entities': [(8, 13, 'DRUG'), (20,36,'MISC')]
    }),

    ("Buenas tardes Luca", {
        'entities': [(14,18,'PER')]
    }),

    ("Linda maria me fume en Roma", {
        'entities': [(6, 11, 'DRUG'), (23,27,'LOC')]
    }),

    ("Volkswagen proviene al igual que Audi de Alemania", {
        'entities': [(0, 10, 'ORG'),(33, 37, 'ORG'), (41, 49, 'LOC')]
    }),

    ("Mario la denomina frula", {
        'entities': [(0, 5, 'PER'), (18, 23, 'DRUG')]
    }),

    ("Nicolás no consume estimulantes", {
        'entities': [(0, 7, 'PER'),(19, 31, 'DRUG')]
    }),

    ("Es hora de prender el faso", {
        'entities': [(22, 26, 'DRUG')]
    }),
    
    ("Las canciones modernas hacen apologia de las drogas", {
        'entities': [(45, 51, 'DRUG')]
    }),
    
    ("Mientras Gaston genera el nuevo modelo sigue escribiendo", {
        'entities': [(9, 15, 'PER')]
    }),
    
    ("si toy labuarando y me vengo máqana xk recien comense desde el lunes y toy cm una semana en Jujuy", {
        'entities': [(3, 6, 'ME'),(7, 17, 'ME'),(29, 35, 'ME'), (36, 38, 'ME'), (46, 53, 'ME'), (71, 74, 'ME'),(75, 77, 'ME'),(92,97,'LOC')]
    }),

    ("yo aka en ksa trab ,,,terminando lo k falta de est porrito", {
        'entities': [(3, 6, 'ME'),(10, 13, 'ME'),(14, 18, 'ME'),(19, 22, 'ME'),(36, 37, 'ME'),(47, 50, 'ME'),(51,58,'DRUG')]
    }),

    ("A ree bien primo que tal el clima aya en Tandil", {
        'entities': [(2, 5, 'ME'),(34, 37, 'ME'),(41, 47, 'LOC')]
    }),

    ("dale capas k venga por un poco de merca luego te aviso okey", {
        'entities': [(11, 12, 'ME'),(34, 39, 'DRUG')]
    }),

    ("Jajaja gil mi vieja no me deja LSD tomar en casa", {
        'entities': [(0, 6, 'ME'),(31, 34, 'DRUG'),(44, 48, 'MISC')]
    }),

    ("de última tomamos coca fue jejeje", {
        'entities': [(18, 22, 'DRUG')]
    }),

    ("bien aka yendo pa mi ksa xq recien salí del trabajo?", {
        'entities': [(5, 8, 'ME'),(15, 17, 'ME'),(21, 24, 'ME'),(25, 27, 'ME'),(44, 51, 'MISC')]
    }),
    
    ("Mm nada aca en mi casa escuchando ganya y vos??", {
        'entities': [(0, 2, 'ME'),(34, 39, 'DRUG')]
    }),
    
    ("eh primo hoy dijo ah romenco recien me llamó Julio?", {
        'entities': [(21, 28, 'LOC'),(45, 50, 'PER')]
    }),
    
    ("todas son lindas ,,,ta pa partírles cm un queso,,,se ponen unas calzas pero mal?", {
        'entities': [(17, 22, 'ME'),(23, 25, 'ME'),(36, 38, 'ME'),(47, 50, 'ME')]
    }),

    ("fumando porro, hola cm taz k hacías", {
        'entities': [(8, 13, 'DRUG'),(20, 22, 'ME'),(23, 27, 'ME'),(28, 29, 'ME')]
    }),

    ("si si la próxima bailamos hasta k salga el sol eaaa jeje", {
        'entities': [(32, 33, 'ME'),(47, 51, 'ME'),(52, 56, 'ME')]
    }),

    ("eh wacho pasame algún num de tus dilers asi los wasapeo jeje?", {
        'entities': [(3, 8, 'ME'),(22, 25, 'ME'),(33, 39, 'DRUG'),(48, 55, 'ME'),(56, 60, 'ME'),]
    }),

    ("wueno Nico te dejo xq voy ah comensar ah drogarme?", {
        'entities': [(0, 5, 'ME'),(6, 10, 'PER'),(19, 21, 'ME'),(29, 37, 'ME'),(41, 49, 'DRUG')]
    }),

    ("y aka andamos más k bien en Google?", {
        'entities': [(2, 5, 'ME'),(18, 19, 'ME'),(28, 34, 'ORG')]
    }),

    ("Si si estbmos d asado jejej si Saul :)", {
        'entities': [(6, 13, 'ME'),(14, 15, 'ME'),(22, 27, 'ME'),(30, 34, 'PER')]
    }),

    ("yo bien aka disfrutando del paco?", {
        'entities': [(8, 11, 'ME'),(28, 32, 'DRUG')]
    }),
    
    ("vs sos de Bolivia no?", {
        'entities': [(0, 2, 'ME'),(10, 17, 'LOC')]
    }),
    
    ("che vs no lo tns mi billetera xk no lo encuentro", {
        'entities': [(4, 6, 'ME'),(13, 16, 'ME'),(30, 32, 'ME')]
    }),
    
    ("y yo aka en lo de Rudy vine ah vicitar xk ya tuvo ah su hija su mujer?", {
        'entities': [(5, 8, 'ME'),(18,22,'PER'),(39, 41, 'ME')]
    }),

    ("k hiciste en el fin de semana", {
        'entities': [(0, 1, 'ME')]
    }),

    ("asta k no empiece a vender el faso", {
        'entities': [(0, 4, 'ME'),(5, 6, 'ME'),(29,33,'DRUG')]
    }),

    ("Alas 8 juego ala pelota. Por Polonia", {
        'entities': [(0, 4, 'ME'),(13, 16, 'ME'),(29, 36, 'LOC')]
    }),

    ("che y al final ahi joda en abruzece o no?", {
        'entities': [(27, 35, 'MISC')]
    }),

    ("tamos en la cumbre festejando el cumple de Elvira?", {
        'entities': [(12, 18, 'MISC'),(43, 49, 'PER')]
    }),

    ("No pasa qe ya estoy en mi trabajo xeso estoy mal", {
        'entities': [(8, 10, 'ME'),(26, 33, 'MISC'),(34, 38, 'ME')]
    }),

    ("ah wueno me imagino k taz re turbina?", {
        'entities': [(3, 8, 'ME'),(20, 21, 'ME'),(22, 25, 'ME'),(29, 36, 'DRUG')]
    }),
    
    ("ahi liyo pal compa", {
        'entities': [(4, 9, 'DRUG'),(9, 12, 'ME'),(13, 18, 'ME')]
    }),
    
    ("le di a la pasta guacho", {
        'entities': [(11, 16, 'DRUG'),(17, 23, 'ME')]
    }),
    
    ("Julio tiene cristales", {
        'entities': [(0,5,'PER'),(12,21,'DRUG')]
    }),

    ("bazuco? en el trabajo", {
        'entities': [(0, 6, 'DRUG'), (14,21,'MISC')]
    }),

    ("En Toyota no venden acido", {
        'entities': [(3,9,'ORG'),(20,25,'DRUG')]
    }),

    ("Ah xq jaja no ay polvo pero", {
        'entities': [(3, 5, 'ME'),(6, 10, 'ME'),(14, 16, 'ME'),(17, 22, 'DRUG')]
    }),

    ("Bn bn aca cocinando perico, va terminando ejje", {
        'entities': [(0, 2, 'ME'),(3, 5, 'ME'),(20, 26, 'DRUG'),(42, 46, 'ME')]
    }),

    ("Carlo la denomina hash", {
        'entities': [(0, 5, 'PER'), (18, 22, 'DRUG')]
    }),

    ("Nicolás no consume estimulantes", {
        'entities': [(0, 7, 'PER'),(19, 31, 'DRUG')]
    }),

    ("dale arrancate un verde y pinta la fiesta", {
        'entities': [(18, 23, 'DRUG')]
    }),
    
    ("tambien tenemos kush", {
        'entities': [(16, 20, 'DRUG')]
    }),
    
    ("alta blancanieves", {
        'entities': [(5, 17, 'DRUG')]
    }),
    
    ("Mabel deja de darle al carton", {
        'entities': [(0, 5, 'PER'),(23, 29, 'DRUG')]
    }),

    ("Q andas haciendo x Facebook? Estas laburando aya?", {
        'entities': [(0, 1, 'ME'),(17, 18, 'ME'),(19, 27, 'ORG'),(45, 48, 'ME')]
    }),
    
    ("Me imagino jeje pero cuand t vs a t casa", {
        'entities': [(11, 15, 'ME'),(27, 28, 'ME'),(29, 31, 'ME'),(34, 35, 'ME'),(36, 40, 'MISC')]
    }),
    
    ("De una no queda otra q laburar la anfeta ", {
        'entities': [(21, 22, 'ME'),(34, 40, 'DRUG')]
    }),

    ("y k me contas de wueno prima", {
        'entities': [(2, 3, 'ME'),(17, 22, 'ME'),]
    }),

    ("Manhattan es una locación", {
        'entities': [(0,9,'LOC')]
    }),

    ("Anita se fumo una kenke, muy gracioso lo de Maria", {
        'entities': [(0, 5, 'PER'), (18,23,'DRUG'), (44, 49, 'PER')]
    }),

    ("jazmin y jamon son denominaciones para lo que buscamos", {
        'entities': [(0, 6, 'DRUG'), (9, 14, 'DRUG')]
    }),

    ("extasis también llamado maka", {
        'entities': [(0, 7, 'DRUG'), (24, 28, 'DRUG')]
    }),

    ("choco, has, goma, ful, china, todas encontradas en Google ", {
        'entities': [(0, 5, 'DRUG'), (7, 10, 'DRUG'), (12, 16, 'DRUG'), (18, 21, 'DRUG'), (23, 28, 'DRUG'), (51, 57, 'ORG')]
    }),

    ("se consigue hongos en la plaza", {
        'entities': [(12, 18, 'DRUG'),(25, 30, 'MISC')]
    }),
    
    ("el elixir de la otra vez", {
        'entities': [(3, 9, 'DRUG')]
    }),
    
    ("rohypnol triene efecto depresor.", {
        'entities': [(0, 8, 'DRUG')]
    }),
    
    ("el valium viene recetado", {
        'entities': [(3, 9, 'DRUG')]
    }),

    ("Marcos consume tachielas", {
        'entities': [(0, 6, 'PER'), (9, 18, 'DRUG')]
    }),

    ("mota, kenke, que mas hay en el campo?", {
        'entities': [(0, 4, 'DRUG'),(6, 11, 'DRUG'),(31, 36, 'MISC')]
    }),

    ("Pablo consumia rulas y mdma", {
        'entities': [(0, 5, 'PER'),(15, 20, 'DRUG'),(23, 27, 'DRUG')]
    }),

    ("se rien del chulas pops", {
        'entities': [(12, 23, 'DRUG')]
    }),

    ("En Francia consumen polen y tate ", {
        'entities': [(3, 10, 'LOC'),(20, 25, 'DRUG'),(28, 32, 'DRUG')]
    }),

    ("Lautaro vendia ful en la escuela", {
        'entities': [(0, 7, 'PER'),(15, 18, 'DRUG'),(25, 32, 'DRUG')]
    }),

    ("un pastel de alta costura", {
        'entities': [(3, 9, 'DRUG'),(18, 25, 'DRUG')]
    }),
    
    ("Ines usa pegamento", {
        'entities': [(0, 4, 'PER'), (9,18,'DRUG')]
    }),

    ("Drogas o sustancias lícitas: se ocupan libremente de acuerdo a los deseos de cada consumidor. Por ejemplo, las bebidas alcohólicas y el tabaco.", {
        'entities': [(0, 6, 'DRUG'), (9, 19, 'DRUG'), (111, 130, 'DRUG'), (136, 142, 'DRUG')]
    }),

    ("Drogas que se utilizan principalmente como medicamento: generalmente se obtienen mediante prescripción médica.", {
        'entities': [(0, 6, 'DRUG'),(43, 54, 'DRUG')]
    }),

    ("En Occidente, su uso va ligado al tratamiento de trastornos del ánimo, trastornos del sueño, enfermedades dolorosas o con el fin de lograr mayor lucidez o concentración (nootrópicos).", {
        'entities': [(170, 181, 'DRUG')]
    }),
    
    ("Por ejemplo, los psicofármacos, estimulantes menores y la metadona.", {
        'entities': [(17, 30, 'DRUG'),(32, 44, 'DRUG'),(58, 66, 'DRUG')]
    }),
    
    ("Drogas o sustancias ilícitas: varían de acuerdo a la legislación de cada país.", {
        'entities': [(0, 6, 'DRUG'),(9, 28, 'DRUG')]
    }),
    
    ("Son aquellas cuyo comercio se considera ilegal, como los derivados cannabis, la heroína y la cocaína.", {
        'entities': [(67, 75, 'DRUG'),(80, 87, 'DRUG'),(93, 100, 'DRUG')]
    }),

    ("Existen convenciones internacionales que han establecido como prohibido el uso no médico de opiáceos, cannabis, alucinógenos, cocaína y muchos otros estimulantes, al igual que de los hipnóticos y sedantes. ", {
        'entities': [(92, 100, 'DRUG'), (102, 110, 'DRUG'), (112, 124, 'DRUG'), (126, 133, 'DRUG'), (149, 161, 'DRUG'), (183, 193, 'DRUG'), (196, 204, 'DRUG')]
    }),
    
    ("Una droga depresora es aquella que ralentiza o inhibe las funciones o la actividad de alguna región del cerebro.", {
        'entities': [(4, 9, 'DRUG')]
    }),
    
    ("Este grupo se subdivide a su vez en varios grupos: antihistamínicos, antipsicóticos, disociativos, GABAnérgicos, glicinérgicos, narcóticos y simpatológicos. ", {
        'entities': [(51, 67, 'DRUG'), (69, 83, 'DRUG'), (85, 97, 'DRUG'), (99, 111, 'DRUG'), (113, 126, 'DRUG'), (128, 138, 'DRUG'), (141, 155, 'DRUG')]
    }),

    ("Una droga estimulante es aquella que produce mejoras temporales de la actividad neurológica o física.", {
        'entities': [(4, 9, 'DRUG')]
    }),

    ("Psicodélicos: producen una alteración en la cognición y la percepción.", {
        'entities': [(0,12,'DRUG')]
    }),

    ("Los psicodélicos suelen agruparse en lisergamidas (destaca el LSD), feniletilaminas, piperazina, triptaminas y otros.", {
        'entities': [(4, 16, 'DRUG'), (37,49,'DRUG'), (62, 65, 'DRUG'), (68, 83, 'DRUG'), (85,95,'DRUG'), (97, 108, 'DRUG')]
    }),

    ("Disociativos: producen un bloqueo de las señales de la mente consciente hacia otras partes del cerebro produciendo alucinaciones, privación sensorial, disociación y trance. ", {
        'entities': [(0, 12, 'DRUG')]
    }),

    ("Se dividen en adamantanos, arilciclohexilaminas y morfinanos.", {
        'entities': [(14, 25, 'DRUG'), (27, 47, 'DRUG'), (50, 60, 'DRUG')]
    }),

    ("Delirantes: producen delirios, a diferencia de los alucinógenos psicodélicos y disociativos en el que se mantiene cierto estado de consciencia ", {
        'entities': [(0, 10, 'DRUG'), (51, 76, 'DRUG'), (79, 91, 'DRUG')]
    }),

    ("Se dividen en anticolinérgicos, antihistamínicos y GABA-agonistas.", {
        'entities': [(14, 30, 'DRUG'),(32, 48, 'DRUG'),(51, 65, 'DRUG')]
    }),
    
    ("Los opioides son las drogas que se unen a receptores opioides situados principalmente en el sistema nervioso central y en el tracto gastrointestinal.", {
        'entities': [(4, 12, 'DRUG'),(21, 27, 'DRUG'),(53, 61, 'DRUG')]
    }),
    
    ("Hay tres grandes clases de sustancias opiáceas: alcaloides del opio, como morfina y codeína;", {
        'entities': [(27, 46, 'DRUG'),(48, 67, 'DRUG'),(74, 81, 'DRUG'),(84, 91, 'DRUG')]
    }),
    
    ("opiáceos semi-sintéticos, tales como heroína y oxicodona", {
        'entities': [(0, 24, 'DRUG'),(37, 44, 'DRUG'),(47, 56, 'DRUG')]
    }),

    ("opioides completamente sintéticos, tales como petidina y metadona", {
        'entities': [(0, 8, 'DRUG'), (46, 54, 'DRUG'), (57, 63, 'DRUG')]
    }),

    ("Para dolores de intensidad fuerte se utilizan opioides fuertes como la morfina, la hidromorfona, la metadona, el fentanilo, etc.?", {
        'entities': [(46, 54, 'DRUG'),(71, 78, 'DRUG'),(83, 95, 'DRUG'),(100, 108, 'DRUG'),(113, 122, 'DRUG')]
    }),

    ("Para el alivio de dolores de intensidad moderada se utilizan opioides débiles, de distribución no libre, como el tramadol, la codeína o la hidrocodona.", {
        'entities': [(61, 69, 'DRUG'),(113, 121, 'DRUG'),(126, 133, 'DRUG'),(139, 150, 'DRUG')]
    }),

    ("Este grupo se divide en subgrupos: etéreos, haloalcanos, opioides y esteroides neuroactivos; inyectables o inhalables.", {
        'entities': [(35, 42, 'DRUG'),(44, 55, 'DRUG'),(57, 65, 'DRUG'),(68, 78, 'DRUG')]
    }),

    ("En Francia consumen polen y tate ", {
        'entities': [(3, 10, 'LOC'),(20, 25, 'DRUG'),(28, 32, 'DRUG')]
    }),

    ("Lautaro vendia ful en la escuela", {
        'entities': [(0, 7, 'PER'),(15, 18, 'DRUG'),(25, 32, 'DRUG')]
    }),

    ("un pastel de alta costura", {
        'entities': [(3, 9, 'DRUG'),(18, 25, 'DRUG')]
    }),
    
    ("Ines usa pegamento", {
        'entities': [(0, 4, 'PER'), (9,18,'DRUG')]
    }),

    ("En ese grupo de mierda que parecia yerba brava o volcan;", {
        'entities': [(35, 40, 'DRUG')]
    }),
    
    ("Quiero ponerme a vivir y un alto faso fumar", {
        'entities': [(33, 37, 'DRUG')]
    }),

    ("no estoy triste no es mi llanto es el humo de este fasito que me hace llorar", {
        'entities': [(51, 57, 'DRUG')]
    }),

    ("Si la plantita se muere por que ya se la fumaron", {
        'entities': [(6, 14, 'DRUG')]
    }),

    ("Mira que loco que quede del churro que me fume", {
        'entities': [(28, 34, 'DRUG')]
    }),

    ("Mira como me has dejado si no me mata la droga me mata tu amor tu amor", {
        'entities': [(41, 46, 'DRUG')]
    }),

    ("Desde que no estas conmigo todo el día tomo vino y no puedo dejar de fumanchar ", {
        'entities': [(69, 78, 'DRUG')]
    }),

    ("Pasame la geringa juana estamos de carabana", {
        'entities': [(10, 17, 'DRUG')]
    }),

    ("qe la banda me responda qe no se acabe la milonga", {
        'entities': [(42, 49, 'DRUG')]
    }),
    
    ("Yo no puedo seguir todo el dia tomando coca que vamo a tomar?", {
        'entities': [(39, 43, 'DRUG')]
    }),

    ("¿Cuánto sale un ladrillo? preguntó un intermediario", {
        'entities': [(16, 24, 'DRUG')]
    }),
    
    (" Nada de pollos ni helados. Es que algunos narcos ni siquiera se preocupan por las posibles grabaciones.", {
        'entities': [(9, 15, 'DRUG'),(19, 16, 'DRUG')]
    }),

    ("Los narcos negocian el abastecimiento de marihuana, pero no se animan a mencionar esa droga para evitar allanamientos.", {
        'entities': [(4, 10, 'DRUG'),(41, 50, 'DRUG'),(86, 91, 'DRUG')]
    }),

    ("Voy a tener que conseguir un poco de lechuga porque me andan pidiendo un montón", {
        'entities': [(37, 44, 'DRUG')]
    }),

    ("Con el Bocha muerto se acabó la buena merca", {
        'entities': [(7,12, 'PER' ),(38, 43, 'DRUG')]
    }),

    ("Cocaína: se puede tomar normalmente por la nariz (inhalado), inyectado con jeringa o por inhalación del humo. ", {
        'entities': [(0, 7, 'DRUG'),(75, 82, 'DRUG')]
    }),

    ("También conocida como: coca, crak, bazuco, perico. ", {
        'entities': [(23, 27, 'DRUG'),(29, 33, 'DRUG'),(35, 41, 'DRUG'), (43, 49, 'DRUG')]
    }),

    ("Si una persona toma Éxtasis, su cuerpo se puede calentar excesiva y peligrosamente mientras baila o practica cualquier otra actividad física.", {
        'entities': [(20, 27, 'DRUG')]
    }),

    ("El Éxtasis se ha convertido en una de las drogas ilegales que más se vende en la calle.", {
        'entities': [(3, 10, 'DRUG'),(42, 48, 'DRUG')]
    }),
    
    ("También se puede llamar:	XTC, E, Eva, Adán, pastillas del amor, X.?", {
        'entities': [(25, 28, 'DRUG'),(30, 31, 'DRUG'),(33, 36, 'DRUG'),(38, 62, 'DRUG'),(64, 66, 'DRUG')]
    }),

    ("El Éxtasis es una droga estimulante que puede provocar alucinaciones.", {
        'entities': [(3, 10, 'DRUG'),(18, 35, 'DRUG')]
    }),
    
    ("Como el Éxtasis, el uso de GHB está muy extendido en los clubs nocturnos y en las fiestas de rave y de música tecno, a las que pueden asistir adolescentes y adultos jóvenes.", {
        'entities': [(8, 18, 'DRUG'),(27, 30, 'DRUG')]
    }),

    ("El GHB provoca tanto un subidón de euforia (intenso incremento de la sensación de felicidad) como alucinaciones.", {
        'entities': [(3, 6, 'DRUG')]
    }),

    ("El GHB ha hecho que mucha gente joven necesite recibir cuidados médicos de urgencia.", {
        'entities': [(3, 6, 'DRUG')]
    }),

    ("La mariguana se fuma como un cigarrillo hecho a mano o envuelto (lo que recibe el nombre de porro o canuto).", {
        'entities': [(3, 12, 'DRUG'),(92, 97, 'DRUG'),(100, 106, 'DRUG')]
    }),

    ("La mariguana dificulta la conciencia del paso del tiempo y la concentración.", {
        'entities': [(3, 12, 'DRUG')]
    }),

    ("Rafael Nadal, máximo favorito al título, se retira de Melbourne Park tras ser eliminado del Abierto de Australia", {
        'entities': [(0, 12, 'PER'),(54, 68,'MISC'),(92, 112, 'MISC')]
    }),

    ("Sólo dos pertenecen al grupo de 10 primeros del ránking ATP, que son Roger Federer, N°2, y Marin Cilic, N°6", {
        'entities': [(69,82, 'PER' ),(91, 102, 'PER')]
    }),

    ("México: especialistas revelaron el verdadero significado de Teotihuacán ", {
        'entities': [(0, 6, 'LOC'),(60, 71, 'MISC')]
    }),

    ("Donald Trump apuntó contra el FBI por la pérdida de miles de mensajes de un funcionario que lo investigaba ", {
        'entities': [(0, 12, 'PER'),(30, 33, 'MISC')]
    }),

    ("Un estudio del Instituto Nacional de Antropología e Historia (INAH) de México reveló que el nombre de la urbe prehispánica de Teotihuacán", {
        'entities': [(15, 77, 'MISC'),(126, 137, 'MISC')]
    }),

    ("El mandatario estadounidense consideró que no haber preservado los intercambios entre Peter Strzok y su pareja, Lisa Page, durante uno de los períodos clave de las pesquisas por la injerencia rusa, es una de las mayores noticias en mucho tiempo", {
        'entities': [(86, 98, 'PER'),(112, 121, 'PER')]
    }),
    
    ("El Frente Renovador va a la Justicia por la inconstitucionalidad del megadecreto de Mauricio Macri", {
        'entities': [(84, 98, 'PER')]
    }),

    ("Mauricio es el presidente de Argentina", {
        'entities': [(0, 8, 'PER'),(29, 38, 'LOC')]
    }),
    
    ("La divisa de EEUU se vende a $19,61 en bancos del microcentro porteño", {
        'entities': [(13, 17, 'LOC'),(39, 69, 'MISC')]
    }),

    ("Sebastián Piñera presentó el gabinete para su segundo mandato al frente de Chile", {
        'entities': [(0, 16, 'PER'),(75, 80, 'LOC')]
    }),

    ("Éste es el caso de Andrés Chadwick en una de las carteras más importantes del gabinete, la de ministro del Interior", {
        'entities': [(19, 34, 'PER'),(94, 115, 'MISC')]
    }),

    ("La mariguana se fuma como un cigarrillo hecho a mano o envuelto (lo que recibe el nombre de porro o canuto).", {
        'entities': [(3, 12, 'DRUG'),(92, 97, 'DRUG'),(100, 106, 'DRUG')]
    }),

    ("La mariguana dificulta la conciencia del paso del tiempo y la concentración.", {
        'entities': [(3, 12, 'DRUG')]
    }),

    ("Ooooja k pasho jeje", {
        'entities': [(0, 6, 'ME'),(7, 8, 'ME'),(9, 14, 'ME'),(15, 19, 'ME')]
    }),

    ("vs si k la pasas re bien cambiando num ehhh ?", {
        'entities': [(0, 2, 'ME'),(6, 7, 'ME'),(35, 38, 'ME'),(39, 43, 'ME')]
    }),

    ("Jajjaja lo blokee sin kerer keriendo jaj", {
        'entities': [(0, 7, 'ME'),(11, 17, 'ME'),(22, 27, 'ME'),(28, 35, 'ME'),(36, 39, 'ME')]
    }),

    ("Jjaja wuen dia primith jaja ", {
        'entities': [(0, 5, 'ME'),(6, 10, 'ME'),(15, 22, 'ME'),(23, 27, 'ME')]
    }),

    ("Mmmm me hces um favore xfavor jajaj", {
        'entities': [(0, 4, 'ME'),(8, 12, 'ME'),(9, 11, 'ME'), (12, 18, 'ME'), (19, 25, 'ME'), (26, 31, 'ME')]
    }),

    ("Ajajja cuango lo pued bajr te dig iwual mchas gracias", {
        'entities': [(0, 6, 'ME'),(7, 13, 'ME'), (17, 21, 'ME'), (22, 26, 'ME'), (30, 33, 'ME'), (34, 39, 'ME'), (40, 44, 'ME')]
    }),
    
    ("Siiiii yege jajja si te envie un maj", {
        'entities': [(0, 6, 'ME'), (7,11,'ME'), (22, 27, 'ME'), (33, 36, 'ME')]
    }),

    ("Ooooh mmm noce xk llego tarde seguro xk no abia colectiv", {
        'entities': [(0, 5, 'ME'),(6, 9, 'ME'),(9, 13, 'ME'), (14,16,'ME'),(37, 39, 'ME'), (43, 47, 'ME'), (48, 56, 'ME')]
    }),
    
    ("Jugamos a las 14:00 aya en Balcarce", {
        'entities': [(20, 23, 'ME'),(27, 35, 'LOC')]
    }),

    ("contam k isiste hoy primita?", {
        'entities': [(0, 6, 'ME'), (7,8,'ME'), (9, 15, 'ME')]
    }),

    ("claro xk ahi días k toy mal y aburrido y noc en kien desaugarme,,", {
        'entities': [(6, 8, 'ME'), (18,19,'ME'), (20, 23, 'ME'), (41, 44, 'ME'), (48,52,'ME'), (53, 63, 'ME'), (63, 65, 'ME')]
    }),

    ("Primo k haces.... todo tranca.?", {
        'entities': [(6, 4, 'ME'), (13,17,'ME'), (23, 29, 'ME')]
    }),

    ("Pero stoy cn diana", {
        'entities': [(5, 9, 'ME'),(10, 12, 'ME'), (13, 18, 'PER')]
    }),

    ("Asta batan voy en remis de ahi me llevas ", {
        'entities': [(0, 4, 'ME'), (5, 10, 'LOC')]
    }),

    ("Ke corta manbos stos borrachos", {
        'entities': [(0, 2, 'ME'), (9,15,'ME'), (16, 20, 'ME')]
    }),

    ("Stoy yebando a mi papa a la cancha despues tengo ke ir a terminar de invitar", {
        'entities': [(0, 4, 'ME'), (5,12,'ME'), (49, 51, 'ME')]
    }),
    
    ("Ke viento se lebanto biento ahora?", {
        'entities': [(0, 2, 'ME'), (13,20,'ME'), (21, 27, 'ME')]
    }),

    ("Mañana voy a pagar la lus y yego un rato si no ay mucha jente", {
        'entities': [(22, 25, 'ME'), (28,32,'ME'), (47, 49, 'ME'), (56, 61, 'ME')]
    }),
    
    (" 123 y sigo voi al hospital a vuscar mi medicacion aver si me la dan", {
        'entities': [(12, 15, 'ME'), (30,36,'ME'), (51, 55, 'ME')]
    }),

    ("Voi x el puemte ya no doi mas", {
        'entities': [(0, 3, 'ME'), (4,5,'ME'), (9, 15, 'ME'), (22, 25, 'ME')]
    }),

    ("Si se vino hoi hace un rato y ya andamos en la calle de transa las dos ji", {
        'entities': [(11, 14, 'ME'), (56,62,'DRUG'), (71, 73, 'ME')]
    }),

    ("Que vas a fumar vos nenA me queda un vagullo solo", {
        'entities': [(20,24, 'ME' ),(37, 44, 'DRUG')]
    }),

    ("No no se recupera mas juan ya dijo el medico anoche estaba agrecibo mal ni los calmante lo paran ", {
        'entities': [(22, 26, 'PER'),(59, 67, 'ME')]
    }),

    ("Viste parece mas joben ", {
        'entities': [(17, 23, 'ME')]
    }),

    ("Ke ases ? Ase frio ahora", {
        'entities': [(0, 2, 'ME'), (3,7,'ME'), (10, 13, 'ME')]
    }),

    ("Y te dava para el escavio", {
        'entities': [(5, 9, 'ME'),(18, 25, 'DRUG')]
    }),
    
    ("Yo tomo un remis y voi para alla x que estoi esperando a sofia", {
        'entities': [(19, 22, 'ME'), (33,34,'ME'), (39, 46, 'ME')]
    }),

    ("El Éxtasis es una droga estimulante que puede provocar alucinaciones.", {
        'entities': [(3, 10, 'DRUG'),(18, 35, 'DRUG')]
    }),
    
    ("Como el Éxtasis, el uso de GHB está muy extendido en los clubs nocturnos y en las fiestas de rave y de música tecno, a las que pueden asistir adolescentes y adultos jóvenes.", {
        'entities': [(8, 18, 'DRUG'),(27, 30, 'DRUG')]
    }),

    ("El GHB provoca tanto un subidón de euforia (intenso incremento de la sensación de felicidad) como alucinaciones.", {
        'entities': [(3, 6, 'DRUG')]
    }),

    ("El GHB ha hecho que mucha gente joven necesite recibir cuidados médicos de urgencia.", {
        'entities': [(3, 6, 'DRUG')]
    }),

    ("La mariguana se fuma como un cigarrillo hecho a mano o envuelto (lo que recibe el nombre de porro o canuto).", {
        'entities': [(3, 12, 'DRUG'),(92, 97, 'DRUG'),(100, 106, 'DRUG')]
    }),

    ("La mariguana dificulta la conciencia del paso del tiempo y la concentración.", {
        'entities': [(3, 12, 'DRUG')]
    }),

    ("Rafael Nadal, máximo favorito al título, se retira de Melbourne Park tras ser eliminado del Abierto de Australia", {
        'entities': [(0, 12, 'PER'),(54, 68,'MISC'),(92, 112, 'MISC')]
    }),

    ("Sólo dos pertenecen al grupo de 10 primeros del ránking ATP, que son Roger Federer, N°2, y Marin Cilic, N°6", {
        'entities': [(69,82, 'PER' ),(91, 102, 'PER')]
    }),

    ("México: especialistas revelaron el verdadero significado de Teotihuacán ", {
        'entities': [(0, 6, 'LOC'),(60, 71, 'MISC')]
    }),

    ("Donald Trump apuntó contra el FBI por la pérdida de miles de mensajes de un funcionario que lo investigaba ", {
        'entities': [(0, 12, 'PER'),(30, 33, 'MISC')]
    }),

    ("Un estudio del Instituto Nacional de Antropología e Historia (INAH) de México reveló que el nombre de la urbe prehispánica de Teotihuacán", {
        'entities': [(15, 77, 'MISC'),(126, 137, 'MISC')]
    }),

    ("El mandatario estadounidense consideró que no haber preservado los intercambios entre Peter Strzok y su pareja, Lisa Page, durante uno de los períodos clave de las pesquisas por la injerencia rusa, es una de las mayores noticias en mucho tiempo", {
        'entities': [(86, 98, 'PER'),(112, 121, 'PER')]
    }),
    
    ("El Frente Renovador va a la Justicia por la inconstitucionalidad del megadecreto de Mauricio Macri", {
        'entities': [(84, 98, 'PER')]
    }),

    ("Mauricio es el presidente de Argentina", {
        'entities': [(0, 8, 'PER'),(29, 38, 'LOC')]
    }),
    
    ("La divisa de EEUU se vende a $19,61 en bancos del microcentro porteño", {
        'entities': [(13, 17, 'LOC'),(39, 69, 'MISC')]
    }),

    ("Sebastián Piñera presentó el gabinete para su segundo mandato al frente de Chile", {
        'entities': [(0, 16, 'PER'),(75, 80, 'LOC')]
    }),

    ("Éste es el caso de Andrés Chadwick en una de las carteras más importantes del gabinete, la de ministro del Interior", {
        'entities': [(19, 34, 'PER'),(94, 115, 'MISC')]
    }),

    ("La mariguana se fuma como un cigarrillo hecho a mano o envuelto (lo que recibe el nombre de porro o canuto).", {
        'entities': [(3, 12, 'DRUG'),(92, 97, 'DRUG'),(100, 106, 'DRUG')]
    }),

    ("La mariguana dificulta la conciencia del paso del tiempo y la concentración.", {
        'entities': [(3, 12, 'DRUG')]
    }),

    ("Estamos las dos con Candela, vamos a comer a tu casa", {
        'entities': [(20, 27, 'PER'), (48, 52, 'MISC')]
    }),

    ("Ah mira ke bueno... Xke c volvio? Mandale salu2 a las 2... Ke bonita la gorda. Cm c yama?", {
        'entities': [(8, 10, 'ME'),(20, 23, 'ME'),(24, 25, 'ME'),(42, 47, 'ME'),(59, 61, 'ME'),(79, 81, 'ME'),(82, 83, 'ME'),(84, 88, 'ME')]
    }),
    
    ("Y c... Pobre negra.. Y la meli n volvio todavia?? Ke lindo nobre. Es re parecida a la agustina d chikita. Tienen whasapp las chikas?", {
        'entities': [(2, 6, 'ME'),(26, 30, 'PER'),(31, 32, 'ME'),(50, 52, 'ME'),(59, 64, 'ME'),(86, 94, 'PER'),(95, 96, 'ME'),(97, 104, 'ME'),(103, 120, 'ME'),(125, 131, 'ME')]
    }),

    ("Preparate mañana para hacer el tuco, que yo hago los ñoquis", {
        'entities': []
    }),

    ("Queres alitas de pollo o carne?", {
        'entities': []
    }),

    ("Hola tia muy feliz cumple no pude ir a saludarte no hai plata y con las manos vacias no voy ni mamada espero que la pases lindo feliz cumple.", {
        'entities': [(52, 55, 'DRUG')]
    }),

    ("Pero voy a comer con la aBUELA ME BAS ACOMPAÑAR AL BANCO TENGO KE RETIRAR EL PIN", {
        'entities': [(24, 80, 'ME')]
    }),






    ("Ete mi numero nuev ja", {
        'entities': [(0, 3, 'ME'),(14, 18, 'ME'),(19, 21, 'ME')]
    }),

    ("naaa acabo de llegar del trab y no pude ver el partido", {
        'entities': [(0, 4, 'ME'),(25, 29,'ME')]
    }),

    ("Jajjja gracias estab re llenooo encina estabams los 4 na mas xk laro se fue a mar del plata ja", {
        'entities': [(0, 7, 'ME'),(15, 20, 'ME'),(24, 31, 'ME'),(32, 38, 'ME'),(39, 47, 'ME'),(54, 56, 'ME'),(57, 61, 'PER'),(78, 91, 'LOC'),(92, 94, 'ME')]
    }),

    ("mmm k raro k llegue tan tarde mmm ya me imagina xk llegó tarde después dice k nooo ", {
        'entities': [(0, 3, 'ME'),(4, 5, 'ME'),(11, 12, 'ME'),(30, 33, 'ME'),(48, 50, 'ME'),(76, 77, 'ME'),(78, 82, 'PER')]
    }),

    ("Che el domingo se juega si o si contra la gloria. ", {
        'entities': [(42, 48, 'MISC')]
    }),

    ("dale okey ,,pero no me dijo naa ever xk me dijo k me iva llamar y también ah rudy?", {
        'entities': [(10, 12, 'ME'),(28, 31, 'ME'),(32, 36, 'PER'),(37, 39, 'ME'),(48, 49, 'ME'),(53, 56, 'ME'),(74, 76, 'ME'),(77, 81, 'PER')]
    }),

    ("Van a venir pajas no?", {
        'entities': []
    }),
    
    ("Toda tu sangre, tus lagrimas, y tu vida.", {
        'entities': []
    }),

    ("Y tambien que envíes miles de mensajes con chistes, los cuales se riegan como pólvora", {
        'entities': []
    }),
    
    ("mmm noooo xk cuando llegue pa mi ksa no taban ,,asi agarré mis kosas y me fui ah jugar", {
        'entities': [(0, 3, 'ME'),(4, 9, 'ME'),(10, 12, 'ME'),(27, 29, 'ME'),(33, 36, 'ME'),(40, 45, 'ME'),(46, 48, 'ME'),(63, 68, 'ME'),(78, 80, 'ME')]
    }),
    
    ("aparte no saben todavia también de lo k choke", {
        'entities': [(38, 39, 'ME'),(40, 45, 'ME')]
    }),
    
    ("Si lo ves a jhoner desile ke me resp los msjs ke le mande", {
        'entities': [(12, 18, 'PER'),(19, 25, 'ME'),(26, 28, 'ME'),(32, 36, 'ME'),(41, 45, 'ME'),(46, 48, 'ME')]
    }),


    

    

]
