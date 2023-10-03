# API Rest Django e SQLite3

 API feita em django e sqlite3 que tem pacientes e variantes, cada paciente pode possuir diversas variantes, e uma variante igual pode estar em diversos pacientes.

 como subir o projeto local:
 
# Passo 1:
  Instalar as dependencias do projeto no ambiente que desejar:
  
    pip install -r requirements. txt 
  
  ou 
  
    pip install django djangorestframework

# Passo 2
  Inicializar o projeto:
  
    python manage.py runserver 

# API tem 2 formas de requisicões

# Insominia ou Postman:

    baseURl: "localhost:8000"

# GET
  Pegar todos os registros:
  
    localhost:8000/pacientes
    
    localhost:8000/variantes
    
  pegar um registro especifico:
                 
    localhost:8000/variantes/(numero do id)
 
    localhost:8000/pacientes/(numero do id)

# POST
  para variantes:
  
    localhost:8000/variantes/
   exemplo:
    
    {		
    	"cromossomo": "chr2",
    	"posicao": 1458,
    	"base_referencia": "A",
    	"base_alternativa": "T"
    }
  para pacientes:
    
    localhost:8000/pacientes/
   exemplo:
    
    {
      "nome": "ulisses",
      "sexo": "M",
      "idade": 51,
      "variantes": [
        "(ID de 1 ou mais Variantes que estejam cadastradas)"
      ]
    }

# PUT
  para paciente:
  
    localhost:8000/pacientes/(id do paciente)/
    
   exemplo:
    ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/c1fb72fc-622f-4a8b-bbaa-dc25950ee4ea)
  
    
  para variantes:
    
    localhost:8000/variantes/(id da variante)/
    
   exemplo:
    ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/2103e4e4-acbe-4281-a1ef-c1b71a061aea)
  
# DELETE
  para paciente:
     
     localhost:8000/pacientes/(id do paciente)/
     
  para variantes:
     
     localhost:8000/variantes/(id da variante)/
  

# Sistema Django
  Ao inicializar o projeto voce podera vizualizar esta tela:
   ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/9c11102e-f133-4ebd-b919-fc52d5ba898c)
  
  Nela vc vai poder acessar as rotas dos pacientes e das variantes:
  ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/bee0fc1b-1366-44ff-9196-4f6f8a0b1085)
  ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/4e245a8d-fb4f-413b-b6f6-0a196c067334)
  
  E vão conseguir aessar os get's para vizualizar e fazer post's para adicionar novos pacientes ou variantes.
  (voce pode selecionar mais e uma variante para o paciente)
  
  para poder atualizar ou deletar um paciente ou uma variante vc deve copiar o seu id e colocar na guia em frente desta maneira:
  
    localhost:8000/pacientes/(numero do id)
  
  e voce sera levado para esta pagina:
  ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/dffd6505-c6f1-401e-9ccf-ac9778e500d4)
  ![image](https://github.com/Harlock221B/desafio-segunda-etapa/assets/64704484/ad17f6dd-97f5-4929-a9d9-2a02bde36d8b)
  
  E podera fazer um put para editar ou deletar as informações da variante ou do paciente.




