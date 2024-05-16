import pytest

def pytest_html_report_title(report):
    report.title = "REPORT TESTES 'EXEMPLO'"
    
def pytest_html_results_summary(prefix):
    prefix.extend([
                   "<img class='logo-empresa' src='C:/Estudos/udemy/Selenium_Modelo_Test/logo/logo-empresa.png' alt='Logo da Empresa'>",
                   
                    
                   ])
    css = """
    <style>
       .logo-empresa {
            width: 124px;
            height: 36px;
            padding: 8px;
            position: absolute; top: 0; left: 1px; 
            background-image: url('C:/Projetos/ONS/ONS_Testes_Selenium/SE-DemandaPiloto/logo/logo_empresa.png');
            background-repeat: no-repeat;
            background-size: contain;
        }
       .logo-cliente {
            width: 250px;
            height: 250px;
            position: absolute;
            top: 35%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-image: url('C:/Projetos/ONS/ONS_Testes_Selenium/SE-DemandaPiloto/logo/logo_cliente.png');
            background-repeat: no-repeat;
            background-size: contain;
            background-position: center, top;
            backdrop-filter: blur(5px);
            z-index: -1;
        }
        body {
            background-color: white;
        }
        #environment {
            color: black;
            background-color: white!important;
        }
        #title {
            text-align: center;
            text-decoration: underline;
        }
        p {
            padding-top: 1px;
        }
        h2 {
            padding-top: 9px;
            text-decoration: underline;
            border: black;
        }
    </style>
    """

    prefix.append(css)

    # Adicione qualquer outro conteúdo HTML que você deseja adicionar ao final do relatório aqui
    prefix.append("""
    <div class="logo-empresa"></div>
    <div class="logo-cliente"></div>
    """)
        

    
    

    