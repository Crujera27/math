<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$localFile = './problems.json';

function readLocalFile($file) {
    if (file_exists($file)) {
        return trim(file_get_contents($file));
    }
    return false;
}

$content = readLocalFile($localFile);
if ($content === false) {
    die("Error: Me he morido sin poder ver el json");
}

$problems = json_decode($content, true);
if (json_last_error() !== JSON_ERROR_NONE) {
    die("Error: Me he morido sin poder etender el json. " . json_last_error_msg());
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>helpme</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-chtml.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2E2E2E;
            color: #E0E0E0;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #6D28D9;
            color: #E0E0E0;
            padding: 20px;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1 {
            color: #F43F5E;
        }
        h2 {
            color: #D946EF;
        }
        .problem {
            background-color: #1F2937;
            border: 1px solid #4B5563;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .solution {
            background-color: #374151;
            border: 1px solid #4B5563;
            border-radius: 8px;
            padding: 15px;
        }
        code {
            background-color: #111827;
            color: #F9A8D4;
            padding: 5px;
            border-radius: 4px;
        }
        a {
            color: #FF00FF;
        }
        .issue-button {
            width: 175px;
            display: inline-flex;
            align-items: center;
            color: #D946EF;
            text-decoration: none;
            font-size: 16px;
            padding: 10px;
            background-color: #1F2937;
            border-radius: 8px;
            border: 1px solid #4B5563;
        }
        .issue-button:hover {
            background-color: #374151;
        }
        .icon-size {
            width: 24px !important;
            height: 24px !important; 
            margin-right: 8px;
        }
        footer {
            background-color: #6D28D9;
            color: #E0E0E0;
            padding: 10px;
            text-align: center;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Problemas muy realistas con mucho potencial para ser un despropósito</h1>
    </header>
    <div class="container">
        <?php if (empty($problems)): ?>
            <p>No se han encontrado problemas</p>
        <?php else: ?>
            <?php foreach ($problems as $problem): ?>
                <div class="problem">
                    <h2><?php echo htmlspecialchars($problem['title']); ?></h2>
                    <p><?php echo htmlspecialchars($problem['description']); ?></p>
                    <?php if (!empty($problem['solution'])): ?>
                        <h3>Solución</h3>
                        <p><?php echo htmlspecialchars($problem['solution']); ?></p>
                    <?php endif; ?>
                    <a href="https://github.com/Crujera27/math/issues/new?title=Informaci%C3%B3n%20err%C3%B3nea%20%2F%20resoluci%C3%B3n%20err%C3%B3nea&body=Por%20favor%2C%20revise%20la%20informaci%C3%B3n%20proporcionada%20para%20el%20problema%20%231%20y%20verifique%20si%20la%20resoluci%C3%B3n%20es%20correcta%2E" class="issue-button" target="_blank">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 mr-2" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                        </svg>
                        Informar sobre información errónea / inadecuada
                    </a>
                </div>
            <?php endforeach; ?>
        <?php endif; ?>
    </div>
    <footer>
        Problemas hechos con imaginación y el poder de las tecnologías.<br>
        &copy; 2024 <a href="https://github.com/Crujera27">Ángel Crujera</a> y contribuidores a <a href="http://github.com/Crujera27/math">github.com/Crujera27/math</a>. Todos los materiales proporcionados en esta web están distribuidos bajo la licencia MIT.
    </footer>
</body>
</html>