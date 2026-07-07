import customtkinter as ctk
import random
from tkinter import messagebox

# ============================================
# BANCO DE PREGUNTAS (120+ preguntas de calidad)
# ============================================

questions_bank = [
    # HISTORIA
    {"q": "¿En qué fecha se celebra la Independencia de El Salvador?", 
     "options": ["15 de septiembre de 1821", "16 de septiembre de 1821", "2 de febrero de 1841", "20 de diciembre de 1983"], "answer": "A"},
    {"q": "¿Dónde se firmó el Acta de Independencia de Centroamérica?", 
     "options": ["San Salvador", "Guatemala", "Ciudad de México", "Tegucigalpa"], "answer": "B"},
    {"q": "¿Quién es considerado el Padre de la Patria en El Salvador?", 
     "options": ["José Simeón Cañas", "José Matías Delgado", "Manuel José Arce", "Francisco Morazán"], "answer": "B"},
    {"q": "¿En qué año se separó El Salvador de la Federación Centroamericana?", 
     "options": ["1821", "1824", "1841", "1983"], "answer": "C"},
    {"q": "¿Quién es conocido como el Padre de la Patria en El Salvador?", 
     "options": ["Manuel José Arce", "José Matías Delgado", "Francisco Morazán", "José Simeón Cañas"], 
     "answer": "B"},
    {"q": "¿Qué fue la Federación Centroamericana?", 
     "options": ["Una alianza militar contra España", "Unión de países centroamericanos de 1823 a 1841", "Un tratado comercial con México", "Una confederación con Estados Unidos"], 
     "answer": "B"},
    {"q": "¿Cuándo entró en vigor la Constitución actual de El Salvador?", 
     "options": ["15 de septiembre de 1821", "2 de febrero de 1841", "20 de diciembre de 1983", "1 de enero de 2001"], 
     "answer": "C"},
    {"q": "¿Qué rol jugó José Matías Delgado en la historia de El Salvador?", 
     "options": ["Primer presidente", "Prócer de la independencia, sacerdote y líder político", "Compositor del himno nacional", "Fundador de la Fuerza Armada"], 
     "answer": "B"},
    {"q": "¿Cuánto tiempo duró aproximadamente la Federación Centroamericana?", 
     "options": ["5 años", "10 años", "18 años", "25 años"], 
     "answer": "C"},
    {"q": "¿Qué fecha marca la independencia absoluta de El Salvador como república soberana?", 
     "options": ["15 de septiembre de 1821", "2 de febrero de 1841", "20 de diciembre de 1983", "1 de enero de 2001"], 
     "answer": "B"},
    {"q": "¿Qué pueblo indígena habitaba principalmente el occidente de El Salvador antes de la conquista española?", 
     "options": ["Mayas", "Pipiles", "Lencas", "Aztecas"], 
     "answer": "B"},
    {"q": "¿Qué producto fue clave en la economía salvadoreña durante el siglo XIX y principios del XX?", 
     "options": ["Banano", "Café", "Algodón", "Cacao"], 
     "answer": "B"},
    {"q": "¿En qué año se anexó temporalmente El Salvador al Imperio Mexicano?", 
     "options": ["1821", "1822", "1823", "1830"], 
     "answer": "B"},
    {"q": "¿Quién fue el primer Presidente de El Salvador como Estado independiente?", 
     "options": ["José Matías Delgado", "Manuel José Arce", "Francisco Morazán", "Juan José Osorio"], 
     "answer": "B"},
    {"q": "¿Qué importante documento se firmó el 15 de septiembre de 1821?", 
     "options": ["La Constitución de El Salvador", "El Acta de Independencia de Centroamérica", "La Constitución de 1983", "El Tratado de Paz"], 
     "answer": "B"},
    {"q": "¿Cuál fue el principal motivo por el que El Salvador se separó de la Federación Centroamericana?", 
     "options": ["Problemas económicos", "Disputas por el poder y diferencias políticas", "Invasión extranjera", "Desastres naturales"], 
     "answer": "B"},
    {"q": "¿Cuándo entró en vigor la Constitución actual de El Salvador?", 
     "options": ["15 de diciembre de 1983", "20 de diciembre de 1983", "16 de diciembre de 1983", "1 de enero de 1984"], "answer": "B"},
    
    # CONSTITUCIÓN Y GOBIERNO
    {"q": "¿Qué mayoría se necesita en la Asamblea Legislativa para reformar la Constitución?", 
     "options": ["Mayoría simple", "Dos tercios de los diputados", "Tres cuartos", "Unanimidad"], "answer": "B"},
    {"q": "¿Cuántos poderes del Estado existen en El Salvador?", 
     "options": ["Dos", "Tres", "Cuatro", "Cinco"], "answer": "B"},
    {"q": "¿Cuántos diputados tiene la Asamblea Legislativa de El Salvador?", 
     "options": ["50", "60", "70", "84"], "answer": "B"},
    {"q": "¿Cuánto dura el período presidencial en El Salvador?", 
     "options": ["4 años", "5 años", "6 años", "7 años"], "answer": "B"},
    {"q": "¿Qué significa que la Constitución de El Salvador es rígida?", 
     "options": ["Que no se puede cambiar nunca", "Que requiere dos tercios de diputados y referéndum para reformarse", "Que solo el presidente puede modificarla", "Que cambia cada 10 años"], 
     "answer": "B"},
    {"q": "¿Qué dice el Artículo 1 de la Constitución de El Salvador?", 
     "options": ["El Salvador es una república", "El Salvador es un Estado soberano, libre e independiente", "Todos son iguales ante la ley", "La soberanía reside en el pueblo"], "answer": "B"},
    {"q": "¿Qué tipo de gobierno tiene El Salvador según su Constitución?", 
     "options": ["Monarquía constitucional", "República democrática presidencialista", "Sistema parlamentario", "Dictadura"], 
     "answer": "B"},
    {"q": "¿Quiénes son considerados próceres de la independencia de El Salvador?", 
     "options": ["José Matías Delgado y Manuel José Arce", "Francisco Morazán y Rafael Carrera", "Augusto Sandino y Farabundo Martí"], 
     "answer": "A"},
    {"q": "¿Dónde reside la soberanía en El Salvador?", 
     "options": ["En el Presidente", "En la Asamblea Legislativa", "En el pueblo salvadoreño", "En el Órgano Judicial"], 
     "answer": "C"},
    {"q": "¿Cuántos años dura el mandato de un diputado de la Asamblea Legislativa?", 
     "options": ["3 años", "4 años", "5 años", "6 años"], 
     "answer": "C"},
    {"q": "¿Cuál es el sistema de gobierno de El Salvador?", 
     "options": ["Monarquía parlamentaria", "Republicano, representativo y democrático", "Sistema socialista", "Dictadura presidencial"], 
     "answer": "B"},
    {"q": "¿Es posible la reelección presidencial inmediata en El Salvador según la Constitución actual?", 
     "options": ["Sí, sin límite", "No, está prohibida", "Solo una vez", "Solo si gana por mayoría absoluta"], 
     "answer": "A"},
    {"q": "¿Cuál es la función principal del Órgano Judicial?", 
     "options": ["Hacer las leyes", "Ejecutar las leyes", "Impartir justicia e interpretar las leyes", "Controlar el presupuesto nacional"], 
     "answer": "C"},
    {"q": "¿Cuál es el idioma oficial de El Salvador?", 
     "options": ["Inglés", "Castellano", "Nahuatl", "Portugués"], 
     "answer": "B"},
    {"q": "¿Quién es el Comandante General de la Fuerza Armada de El Salvador?", 
     "options": ["El Ministro de Defensa", "El Presidente de la República", "El Jefe del Estado Mayor", "El Ministro del Interior"], 
     "answer": "B"},
    {"q": "¿Cuáles son tres fiestas patronales importantes de El Salvador?", 
     "options": ["Carnaval de San Miguel, Fiestas Julias de Santa Ana y Fiestas del Divino Salvador del Mundo", "Festival de la Flor, Feria del Maíz y Día del Árbol", "Semana Santa, Navidad y Año Nuevo"], 
     "answer": "A"},
    {"q": "¿En qué año se firmaron los Acuerdos de Paz en El Salvador?", 
     "options": ["1989", "1990", "1992", "1994"], 
     "answer": "C"},
    {"q": "¿Qué es un referéndum?", 
     "options": ["Una ley del presidente", "Una votación popular para aprobar o rechazar algo importante", "Un tipo de impuesto", "Una reunión de diputados"], "answer": "B"},
    
    # SÍMBOLOS PATRIOS
    {"q": "¿Cuáles son los colores de la bandera de El Salvador?", 
     "options": ["Rojo, blanco y azul", "Azul, blanco y azul", "Verde, blanco y azul", "Amarillo, azul y blanco"], "answer": "B"},
    {"q": "¿Qué representa el color blanco de la bandera?", 
     "options": ["El mar", "La libertad", "La paz", "La riqueza"], "answer": "C"},
    {"q": "¿Qué palabras aparecen en la base del Escudo Nacional?", 
     "options": ["Libertad, Igualdad, Fraternidad", "Dios, Unión y Libertad", "Patria, Pueblo y Ley", "Justicia y Paz"], "answer": "B"},
    {"q": "¿Cuántos volcanes aparecen en el Escudo Nacional?", 
     "options": ["Tres", "Cuatro", "Cinco", "Siete"], "answer": "C"},
    {"q": "¿Qué representa el gorro frigio (gorro rojo) del escudo?", 
     "options": ["La paz", "La libertad", "La igualdad", "La unión"], "answer": "B"},
    {"q": "¿Qué significan los colores de la bandera de El Salvador?", 
     "options": ["Azul: cielo y mar Pacífico / Blanco: paz", "Azul: libertad / Blanco: igualdad", "Rojo: sangre / Blanco: paz", "Verde: esperanza / Blanco: pureza"], 
     "answer": "A"},
    {"q": "¿Qué representan los cinco volcanes en el Escudo Nacional?", 
     "options": ["Los cinco departamentos más grandes", "Los cinco países de Centroamérica", "Los cinco ríos principales", "Los cinco presidentes más importantes"], 
     "answer": "B"},
    {"q": "¿Quién escribió la Oración a la Bandera de El Salvador?", 
     "options": ["Juan José Cañas", "Rafael Olmedo", "David Guzmán", "José Matías Delgado"], 
     "answer": "C"},
    {"q": "¿Cuál es la diferencia entre la bandera civil y la bandera oficial?", 
     "options": ["La civil tiene escudo y la oficial no", "La civil solo tiene las tres franjas y la oficial incluye el escudo", "La civil es más grande", "No hay diferencia"], 
     "answer": "B"},
    {"q": "¿Quiénes compusieron el Himno Nacional de El Salvador?", 
     "options": ["Juan Aberle (música) y Rafael Olmedo (letra)", "Juan José Cañas (letra) y Rafael Olmedo (música)", "David Guzmán y Juan Aberle", "Solo Juan José Cañas"], 
     "answer": "B"},
    {"q": "¿Qué representa el laurel en el Escudo Nacional?", 
     "options": ["La paz", "La victoria y los 14 departamentos", "La riqueza agrícola", "La libertad"], 
     "answer": "B"},
    {"q": "¿Qué representa el sol naciente en el Escudo Nacional?", 
     "options": ["El fin de una era", "Nuevo amanecer de la patria", "El poder del presidente", "La riqueza del mar"], 
     "answer": "B"},
    {"q": "¿Qué representa el arco iris en el Escudo Nacional?", 
     "options": ["La guerra", "La paz", "La riqueza", "El futuro"], "answer": "B"},
    {"q": "¿Cuál es el ave nacional de El Salvador?", 
     "options": ["El quetzal", "El torogoz", "El zorzal", "El tucán"], "answer": "B"},
    {"q": "¿Quién compuso la música del Himno Nacional de El Salvador?", 
     "options": ["Juan José Cañas", "Rafael Olmedo", "Juan Aberle", "David Guzmán"], 
     "answer": "C"},
    {"q": "¿Quién escribió la letra del Himno Nacional de El Salvador?", 
     "options": ["Rafael Olmedo", "Juan Aberle", "Juan José Cañas", "David Guzmán"], 
     "answer": "C"},
    {"q": "¿Cuál es la flor nacional de El Salvador?", 
     "options": ["La rosa", "El izote", "La orquídea", "El girasol"], "answer": "B"},
    {"q": "¿Cuál es el árbol nacional de El Salvador?", 
     "options": ["El ciprés", "El maquilishuat", "El cedro", "El mango"], "answer": "B"},
    {"q": "¿Qué representa el triángulo equilátero del escudo?", 
     "options": ["Los tres poderes del Estado", "Igualdad, libertad y orden", "Los tres océanos", "Las tres razas"], "answer": "B"},
    
    # DEPARTAMENTOS Y GEOGRAFÍA
    {"q": "¿Cuántos departamentos tiene El Salvador?", 
     "options": ["12", "13", "14", "15"], "answer": "C"},
    {"q": "¿Cuál es la capital de El Salvador?", 
     "options": ["Santa Ana", "San Miguel", "San Salvador", "Ahuachapán"], "answer": "C"},
    {"q": "¿En qué departamento se encuentran las ruinas de Tazumal?", 
     "options": ["San Salvador", "Santa Ana", "Ahuachapán", "La Libertad"], "answer": "B"},
    {"q": "¿Cuáles son los departamentos del occidente de El Salvador?", 
     "options": ["San Miguel, Morazán y La Unión", "Ahuachapán, Santa Ana y Sonsonate", "San Salvador, La Libertad y Cuscatlán", "Usulután, San Vicente y Cabañas"], "answer": "B"},
    {"q": "¿Cuál es el río más importante de El Salvador?", 
     "options": ["Río Lempa", "Río Grande", "Río San Miguel", "Río Paz"], "answer": "A"},
    {"q": "¿En qué departamento se encuentra la ciudad de Ahuachapán?", 
     "options": ["Santa Ana", "Sonsonate", "Ahuachapán", "La Libertad"], 
     "answer": "C"},
    {"q": "¿Cuáles son los dos países con los que El Salvador comparte frontera terrestre?", 
     "options": ["Guatemala y Nicaragua", "Guatemala y Honduras", "Honduras y Nicaragua", "Guatemala y Costa Rica"], 
     "answer": "B"},
    {"q": "¿Cuál es el océano que baña las costas de El Salvador?", 
     "options": ["Atlántico", "Pacífico", "Índico", "Caribe"], 
     "answer": "B"},
    {"q": "¿Cuál es la playa más famosa para practicar surf en El Salvador?", 
     "options": ["Costa del Sol", "El Tunco", "Playa Majahual", "El Zonte"], 
     "answer": "B"},
    {"q": "¿Qué zona de El Salvador es conocida como la 'Ruta de las Flores'?", 
     "options": ["Zona oriental", "Occidente (Juayúa, Ataco, Apaneca)", "Zona norte", "Costa del Sol"], 
     "answer": "B"},
    {"q": "¿Cuál es la superficie aproximada de El Salvador?", 
     "options": ["15,000 km²", "21,000 km²", "28,000 km²", "35,000 km²"], 
     "answer": "B"},
    {"q": "¿Cuál es el volcán más conocido de El Salvador?", 
     "options": ["Volcán San Miguel", "Volcán Izalcó (Faro del Pacífico)", "Volcán Santa Ana", "Volcán Boquerón"], 
     "answer": "B"},
    {"q": "¿Aproximadamente cuántos volcanes tiene El Salvador?", 
     "options": ["Menos de 10", "Más de 20 (varios activos)", "Exactamente 14", "Más de 50"], 
     "answer": "B"},
    {"q": "¿Cuál es el departamento más poblado de El Salvador?", 
     "options": ["Santa Ana", "San Miguel", "San Salvador", "La Libertad"], 
     "answer": "C"},
    {"q": "¿Cuántos departamentos hay en el occidente de El Salvador?", 
     "options": ["2", "3", "4", "5"], 
     "answer": "B"},
    {"q": "¿Cuántos departamentos hay en el oriente de El Salvador?", 
     "options": ["3", "4", "5", "6"], 
     "answer": "B"},
    {"q": "¿Cuál es el volcán conocido como el 'Faro del Pacífico'?", 
     "options": ["Volcán San Miguel", "Volcán Santa Ana", "Volcán Izalcó", "Volcán Boquerón"], 
     "answer": "C"},
    {"q": "¿Cuál es el río más importante y largo de El Salvador?", 
     "options": ["Río Paz", "Río Goascorán", "Río Lempa", "Río Grande de San Miguel"], 
     "answer": "C"},
    {"q": "¿Cuál es uno de los lagos más importantes de El Salvador?", 
     "options": ["Lago Atitlán", "Lago de Coatepeque", "Lago Nicaragua", "Lago Gatún"], 
     "answer": "B"},
    {"q": "¿Cuál es la cabecera departamental del departamento de Morazán?", 
     "options": ["Santa Tecla", "San Francisco Gotera", "Zacatecoluca", "Sensuntepeque"], 
     "answer": "B"},
    {"q": "¿Cuál es la cabecera departamental del departamento de La Libertad?", 
     "options": ["Santa Tecla", "Nuevo Cuscatlán", "Antiguo Cuscatlán", "Colón"], 
     "answer": "A"},
    {"q": "¿Cuál es la capital del departamento de Santa Ana?", 
     "options": ["Sonsonate", "Santa Ana", "Chalchuapa", "Ahuachapán"], 
     "answer": "B"},
    {"q": "¿En qué departamento se encuentra el Volcán de Izalcó?", 
     "options": ["San Miguel", "Santa Ana", "La Unión", "Usulután"], 
     "answer": "B"},
    {"q": "¿Cuántos municipios tiene El Salvador?", 
     "options": ["32", "44", "56", "262"], 
     "answer": "B"},
    {"q": "¿Cuántos distritos tiene El Salvador?", 
     "options": ["44", "100", "200", "262"], 
     "answer": "D"},
    {"q": "¿Qué océano baña las costas de El Salvador?", 
     "options": ["Atlántico", "Pacífico", "Índico", "Ártico"], 
     "answer": "B"},
    {"q": "¿Cuál es la cabecera departamental del departamento de La Paz?", 
     "options": ["Santa Tecla", "Zacatecoluca", "San Francisco Gotera", "Sonsonate"], 
     "answer": "B"},
    {"q": "¿Cuál es el departamento más grande de El Salvador por extensión territorial?", 
     "options": ["San Salvador", "La Unión", "Chalatenango", "Usulután"], 
     "answer": "C"},
    {"q": "¿Dónde se encuentran las ruinas arqueológicas de Joya de Cerén?", 
     "options": ["Santa Ana", "San Salvador", "La Libertad", "Cuscatlán"], 
     "answer": "B"},
    {"q": "¿Cuál es el punto más alto de El Salvador?", 
     "options": ["Volcán de Izalco", "Cerro El Pital", "Volcán San Miguel", "Volcán de Santa Ana"], "answer": "B"},
    
    # CULTURA Y ACTUALIDAD
    {"q": "¿Cuál es la moneda oficial de El Salvador desde el año 2001?", 
     "options": ["El colón", "El dólar estadounidense", "El euro", "El bitcoin"], "answer": "B"},
    {"q": "¿Desde qué año es el dólar la moneda oficial de El Salvador?", 
     "options": ["1999", "2000", "2001", "2002"], "answer": "C"},
    {"q": "¿Cuál es la comida típica más representativa de El Salvador?", 
     "options": ["Las baleadas", "Las pupusas", "Los tamales", "El ceviche"], "answer": "B"},
    {"q": "¿Qué significa el Día del Salvador del Mundo?", 
     "options": ["La independencia", "La fiesta patronal de San Salvador", "El día de la Constitución", "El día de los volcanes"], "answer": "B"},
    {"q": "¿Cuál es el plato típico más representativo de El Salvador?", 
     "options": ["Las baleadas", "Las pupusas", "Los tamales", "El ceviche"], 
     "answer": "B"},
    {"q": "¿Qué importancia tiene Bitcoin en El Salvador?", 
     "options": ["Es solo una inversión", "Es moneda de curso legal desde 2021", "Solo se usa en turismo", "Está prohibido"], 
     "answer": "B"},
    {"q": "¿Qué es Surf City?", 
     "options": ["Un centro comercial", "Un proyecto turístico de playas y surf", "Un festival de música", "Un parque nacional"], 
     "answer": "B"},
    {"q": "¿Qué es el maquilishuat?", 
     "options": ["Un volcán", "El árbol nacional de El Salvador", "Una flor típica", "Un plato tradicional"], 
     "answer": "B"},
    {"q": "¿Qué significa el lema nacional 'Dios, Unión y Libertad'?", 
     "options": ["Es solo decorativo", "Es el lema nacional de El Salvador", "Es el nombre de un partido político", "Es el título del himno"], 
     "answer": "B"},
    {"q": "¿Cuáles son tres comidas típicas salvadoreñas?", 
     "options": ["Pupusas, riguas y atol", "Tacos, burritos y enchiladas", "Paella, tortilla y arroz con pollo", "Empanadas, tamales y baleadas"], 
     "answer": "A"},
    {"q": "¿Cuáles son los equipos de fútbol con más trayectoria en El Salvador?", 
     "options": ["Alianza FC, FAS, Firpo y Águila", "Isidro Metapán, Once Municipal y Limeño", "Dragón, Atlético Marte y Chinameca"], 
     "answer": "A"},
    {"q": "¿Quién es conocido como 'El Mágico' en el fútbol salvadoreño?", 
     "options": ["Raúl Díaz Arce", "Jorge Alberto González Barillas", "Hugo Pérez", "Óscar Larios"], 
     "answer": "B"},
    {"q": "¿Qué deporte es el más popular en El Salvador?", 
     "options": ["Béisbol", "Fútbol", "Baloncesto", "Voleibol"], 
     "answer": "B"},
    {"q": "¿Cómo se divide el clima en El Salvador?", 
     "options": ["Cuatro estaciones", "Dos estaciones: seca y lluviosa", "Solo estación lluviosa", "Clima desértico todo el año"], 
     "answer": "B"},
    {"q": "¿Por qué se le conoce a El Salvador como el 'Valle de las Hamacas'?", 
     "options": ["Por sus hermosos valles", "Por su alta actividad sísmica y volcánica", "Por sus hamacas artesanales", "Por su forma geográfica"], 
     "answer": "B"},
    {"q": "¿Cuál es uno de los sitios arqueológicos más importantes de El Salvador?", 
     "options": ["Chichén Itzá", "Joya de Cerén", "Machu Picchu", "Tikal"], 
     "answer": "B"},
    {"q": "¿Cuándo se celebra el Día Nacional de las Pupusas?", 
     "options": ["Segundo domingo de noviembre", "15 de septiembre", "Primer domingo de agosto", "25 de diciembre"], 
     "answer": "A"},
    {"q": "¿Cuáles son tres fiestas importantes de El Salvador?", 
     "options": ["Fiestas Agostinas, Carnaval de San Miguel y Fiestas Julias", "Carnaval de Barranquilla, Feria de las Flores y Oktoberfest", "Día de Muertos, Feria de San Marcos y Inti Raymi"], 
     "answer": "A"},
    {"q": "¿Qué ciudad es conocida como la 'Ciudad Morena'?", 
     "options": ["San Miguel", "Santa Ana", "San Salvador", "Sonsonate"], 
     "answer": "B"},
    {"q": "¿Cuáles son dos aeropuertos importantes de El Salvador?", 
     "options": ["Ilopango y Monseñor Óscar Arnulfo Romero", "Comalapa y Toncontín", "Juan Santamaría y La Aurora"], 
     "answer": "A"},
    {"q": "¿Cuál es uno de los parques nacionales más importantes de El Salvador?", 
     "options": ["Parque Nacional El Imposible", "Parque Yellowstone", "Parque Torres del Paine", "Parque Banff"], 
     "answer": "A"},
    {"q": "¿Qué departamento es conocido por su alta producción de café de calidad?", 
     "options": ["La Unión", "Santa Ana y Ahuachapán", "La Paz", "Morazán"], 
     "answer": "B"},
    {"q": "¿Cuáles son tres cultivos predominantes en El Salvador?", 
     "options": ["Arroz, trigo y soya", "Maíz, caña de azúcar y café", "Banano, piña y coco", "Algodón, tabaco y cacao"], 
     "answer": "B"},
    {"q": "¿Cuáles son los dos cuerpos de seguridad pública y defensa nacional en El Salvador?", 
     "options": ["Policía Nacional Civil y Fuerza Armada", "Guardia Nacional y Ejército", "Policía y Marina", "Fuerza Armada y Inteligencia"], 
     "answer": "A"},
    {"q": "¿Qué es la 'Zafra' en El Salvador?", 
     "options": ["Un festival cultural", "El periodo de cosecha y molienda de la caña de azúcar", "Una danza tradicional", "Un tipo de pupusa"], 
     "answer": "B"},
    {"q": "¿Qué es 'Surf City' en El Salvador?", 
     "options": ["Un parque de diversiones", "Un proyecto turístico de playas y surf", "Un centro comercial", "Un festival de música"], 
     "answer": "B"},
    {"q": "¿Desde qué año el Bitcoin es moneda de curso legal en El Salvador?", 
     "options": ["2019", "2020", "2021", "2022"], 
     "answer": "C"},
    {"q": "¿Quién es el actual Presidente de El Salvador (2026)?", 
     "options": ["Mauricio Funes", "Salvador Sánchez Cerén", "Nayib Bukele", "Hugo Martínez"], 
     "answer": "C"},
    {"q": "¿Qué día se celebra el Día del Salvador del Mundo?", 
     "options": ["15 de septiembre", "6 de agosto", "2 de febrero", "12 de octubre"], 
     "answer": "B"},
    {"q": "¿Qué significa el nombre 'Cuscatlán'?", 
     "options": ["Tierra de volcanes", "Lugar de joyas o tesoros", "País de lagos", "Tierra fértil"], 
     "answer": "B"},
    {"q": "¿Cuál es una de las fiestas patronales más importantes de El Salvador?", 
     "options": ["Feria de San Miguel", "Fiestas Agostinas (Salvador del Mundo)", "Feria de Santa Ana", "Festival del Maíz"], 
     "answer": "B"},
    {"q": "¿Qué tipo de baile tradicional salvadoreño es muy conocido?", 
     "options": ["Cumbia", "Tango", "Xuc", "Salsa"], 
     "answer": "C"},
    {"q": "¿Qué es el 'Torogoz' además de ser el ave nacional?", 
     "options": ["Un volcán", "Un plato típico", "Un símbolo de libertad", "Un tipo de árbol"], 
     "answer": "C"},
    {"q": "¿En qué año se adoptó el dólar estadounidense como moneda oficial?", 
     "options": ["1999", "2000", "2001", "2002"], 
     "answer": "C"},
    {"q": "¿Qué significa 'País de los Volcanes'?", 
     "options": ["Tiene más de 20 volcanes", "Es el país más montañoso", "Sus volcanes son activos", "Es famoso por erupciones"], 
     "answer": "A"},
    {"q": "¿Cuál es el gentilicio correcto de las personas de El Salvador?", 
     "options": ["Salvadorense", "Salvadoreño", "Cuscatleco", "Centroamericano"], 
     "answer": "B"},
    {"q": "¿Qué es Joya de Cerén conocida como?", 
     "options": ["La Pompeya de las Américas", "La Ciudad Maya más grande", "El Volcán Dormido", "La Capital Colonial"], 
     "answer": "A"},
    {"q": "¿Qué bebida típica salvadoreña se hace a base de maíz?", 
     "options": ["Atol de elote", "Café", "Horchata", "Fresco de tamarindo"], 
     "answer": "A"},
    {"q": "¿Por qué se le llama a El Salvador 'País de los Volcanes'?", 
     "options": ["Por sus muchos volcanes", "Por su forma de mapa", "Por su gente explosiva", "Por el maquilishuat"], "answer": "A"},
    {"q": "¿Cuál es el gentilicio de los habitantes de El Salvador?", 
     "options": ["Salvadorense", "Salvadoreño", "Centroamericano", "Cuscatleco"], "answer": "B"},
]

# Colores bonitos (inspirados en la bandera)
BLUE_DARK = "#003087"
BLUE_LIGHT = "#0077B6"
WHITE = "#FFFFFF"
ACCENT = "#00B4D8"

class QuizApp(ctk.CTk):
    def __init__(self):
        self.current_index = 0
        self.score = 0
        self.user_answers = []
        self.time_remaining = 3600  # 60 minutos en segundos
        self.timer_label = None
        self.timer_running = False
        super().__init__()
        self.title("Examen de Naturalización - El Salvador 🇸🇻")
        self.geometry("900x650")
        self.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.current_questions = []
        self.current_index = 0
        self.score = 0
        self.user_answers = []
        
        self.create_welcome_screen()
    
    def create_welcome_screen(self):
        self.clear_screen()
        
        # Título principal
        title = ctk.CTkLabel(self, text="🇸🇻 Examen de Naturalización", 
                             font=ctk.CTkFont(size=32, weight="bold"), text_color=BLUE_LIGHT)
        title.pack(pady=(60, 10))
        
        subtitle = ctk.CTkLabel(self, text="República de El Salvador", 
                                font=ctk.CTkFont(size=20), text_color="gray")
        subtitle.pack(pady=5)
        
        info = ctk.CTkLabel(self, text="25 preguntas de selección múltiple\nHistoria • Constitución • Símbolos • Geografía • Cultura", 
                            font=ctk.CTkFont(size=16), justify="center")
        info.pack(pady=30)
        
        start_btn = ctk.CTkButton(self, text="Comenzar Examen", 
                                  command=self.start_quiz,
                                  font=ctk.CTkFont(size=20, weight="bold"),
                                  height=55, width=280, corner_radius=12,
                                  fg_color=BLUE_DARK, hover_color=BLUE_LIGHT)
        start_btn.pack(pady=40)
        
        note = ctk.CTkLabel(self, text="Preparado para tu proceso de naturalización", 
                            font=ctk.CTkFont(size=14), text_color="gray")
        note.pack(pady=20)
    
    def start_quiz(self):
        self.clear_screen()
        
        # Seleccionar 25 preguntas
        self.current_questions = random.sample(questions_bank, 25)
        self.current_index = 0
        self.score = 0
        self.user_answers = []
        self.time_remaining = 3600  # Reinicia a 60 minutos
        
        self.timer_running = True
        self.create_quiz_screen()
        self.update_timer()  # Inicia el temporizador
    
    def create_quiz_screen(self):
        self.clear_screen()
        
        # Barra de progreso
        progress_text = f"Pregunta {self.current_index + 1} de 25"
        self.progress_label = ctk.CTkLabel(self, text=progress_text, 
                                           font=ctk.CTkFont(size=16, weight="bold"))
        self.progress_label.pack(pady=(20, 5))
        
        self.progress_bar = ctk.CTkProgressBar(self, width=700, height=20)
        self.progress_bar.set((self.current_index) / 25)
        self.progress_bar.pack(pady=5)
        
        # Temporizador
        self.timer_label = ctk.CTkLabel(self, text="Tiempo restante: 60:00", 
                                        font=ctk.CTkFont(size=18, weight="bold"),
                                        text_color=ACCENT)
        self.timer_label.pack(pady=5)

        # Pregunta
        q_data = self.current_questions[self.current_index]
        question_text = q_data["q"]
        
        self.question_label = ctk.CTkLabel(self, text=question_text, 
                                           font=ctk.CTkFont(size=20, weight="bold"),
                                           wraplength=800, justify="center")
        self.question_label.pack(pady=(40, 30))
        
        # Opciones
        self.selected_option = ctk.StringVar()
        
        options_frame = ctk.CTkFrame(self, fg_color="transparent")
        options_frame.pack(pady=10)
        
        letters = ["A", "B", "C", "D"]
        for i, option in enumerate(q_data["options"]):
            btn = ctk.CTkRadioButton(options_frame, 
                                     text=f"{letters[i]}. {option}",
                                     variable=self.selected_option,
                                     value=letters[i],
                                     font=ctk.CTkFont(size=18),
                                     radiobutton_width=22, radiobutton_height=22)
            btn.pack(anchor="w", pady=12, padx=40)
        
        # Botón Siguiente
        self.next_btn = ctk.CTkButton(self, text="Siguiente →", 
                                      command=self.next_question,
                                      font=ctk.CTkFont(size=18, weight="bold"),
                                      height=50, width=200, corner_radius=10,
                                      fg_color=BLUE_DARK, hover_color=BLUE_LIGHT,
                                      state="disabled")
        self.next_btn.pack(pady=30)
        
        # Habilitar botón cuando se seleccione una opción
        self.selected_option.trace_add("write", lambda *args: self.next_btn.configure(state="normal"))
    
    def update_timer(self):
        if not self.timer_running or self.time_remaining <= 0:
            self.time_up()
            return
        
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_text = f"Tiempo restante: {minutes:02d}:{seconds:02d}"
        
        if self.timer_label:
            self.timer_label.configure(text=time_text)
        
        # Cambiar color cuando quede poco tiempo
        if self.time_remaining <= 300:  # Últimos 5 minutos
            self.timer_label.configure(text_color="red")
        
        self.time_remaining -= 1
        self.after(1000, self.update_timer)  # Actualiza cada segundo

    def time_up(self):
        self.timer_running = False
        messagebox.showwarning("⏰ Tiempo terminado", 
                              "Se acabó el tiempo del examen.\n\nTu resultado se guardará.")
        self.show_results()

    def next_question(self):
        if not self.selected_option.get():
            return
        
        q_data = self.current_questions[self.current_index]
        correct = q_data["answer"]
        user_choice = self.selected_option.get()
        
        is_correct = (user_choice == correct)
        if is_correct:
            self.score += 1
        
        self.user_answers.append({
            "question": q_data["q"],
            "user": user_choice,
            "correct": correct,
            "options": q_data["options"],
            "is_correct": is_correct
        })
        
        self.current_index += 1
        
        if self.current_index < 25:
            self.create_quiz_screen()
        else:
            self.show_results()
    
    def show_results(self):
        self.clear_screen()
        
        percentage = (self.score / 25) * 100
        
        # Título de resultados
        title = ctk.CTkLabel(self, text="¡Examen Finalizado!", 
                             font=ctk.CTkFont(size=28, weight="bold"), text_color=BLUE_LIGHT)
        title.pack(pady=(30, 10))
        
        # Puntuación grande
        score_text = f"{self.score} / 25"
        score_label = ctk.CTkLabel(self, text=score_text, 
                                   font=ctk.CTkFont(size=48, weight="bold"))
        score_label.pack(pady=5)
        
        perc_label = ctk.CTkLabel(self, text=f"{percentage:.0f}% de aciertos", 
                                  font=ctk.CTkFont(size=22))
        perc_label.pack(pady=5)
        
        if percentage >= 80:
            msg = "¡Excelente! Estás muy bien preparado."
            color = "#00C853"
        elif percentage >= 60:
            msg = "Buen resultado. Sigue repasando un poco más."
            color = "#FFB300"
        else:
            msg = "Necesitas repasar más. ¡Tú puedes!"
            color = "#FF5252"
        
        msg_label = ctk.CTkLabel(self, text=msg, font=ctk.CTkFont(size=16), text_color=color)
        msg_label.pack(pady=15)
        
        # Botones
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        review_btn = ctk.CTkButton(btn_frame, text="Ver respuestas incorrectas", 
                                   command=self.show_review,
                                   font=ctk.CTkFont(size=16), height=45, width=220)
        review_btn.grid(row=0, column=0, padx=10)
        
        restart_btn = ctk.CTkButton(btn_frame, text="Hacer otro examen", 
                                    command=self.start_quiz,
                                    font=ctk.CTkFont(size=16), height=45, width=180,
                                    fg_color="#2E7D32", hover_color="#1B5E20")
        restart_btn.grid(row=0, column=1, padx=10)
        
        exit_btn = ctk.CTkButton(btn_frame, text="Salir", 
                                 command=self.destroy,
                                 font=ctk.CTkFont(size=16), height=45, width=120,
                                 fg_color="#C62828", hover_color="#B71C1C")
        exit_btn.grid(row=0, column=2, padx=10)
    
    def show_review(self):
        review_window = ctk.CTkToplevel(self)
        review_window.title("Respuestas Incorrectas")
        review_window.geometry("850x600")
        
        scroll_frame = ctk.CTkScrollableFrame(review_window, width=800, height=550)
        scroll_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        wrong_answers = [a for a in self.user_answers if not a["is_correct"]]
        
        if not wrong_answers:
            ctk.CTkLabel(scroll_frame, text="¡Felicidades! No tuviste errores 🎉", 
                         font=ctk.CTkFont(size=20)).pack(pady=50)
            return
        
        for i, ans in enumerate(wrong_answers, 1):
            frame = ctk.CTkFrame(scroll_frame)
            frame.pack(fill="x", pady=8, padx=10)
            
            ctk.CTkLabel(frame, text=f"{i}. {ans['question']}", 
                         font=ctk.CTkFont(size=15, weight="bold"), wraplength=750).pack(anchor="w", padx=15, pady=(10,5))
            
            letters = ["A", "B", "C", "D"]
            for j, opt in enumerate(ans["options"]):
                letter = letters[j]
                if letter == ans["correct"]:
                    text = f"✓ {letter}. {opt}  ← Respuesta correcta"
                    color = "#00C853"
                else:
                    text = f"   {letter}. {opt}"
                    color = "gray"
                
                ctk.CTkLabel(frame, text=text, font=ctk.CTkFont(size=14), 
                             text_color=color).pack(anchor="w", padx=25)
            
            ctk.CTkLabel(frame, text="").pack()  # Espacio
    
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

# ============================================
# INICIAR LA APLICACIÓN
# ============================================
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()