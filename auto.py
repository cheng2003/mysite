import typer
import os  
app = typer.Typer()
     
@app.command()  
def run(name: str):          
    os.system("docker build -t systemapi .")    
    
@app.command() 
def build_run():     
    os.system("docker build -t systemapi .")     
    os.system("docker rm -f systemapi")     
    os.system("docker run -d --name systemapi -p 8000:8000 systemapi:latest")     
    os.system("start http://192.168.99.100:8000/docs")  

@app.command() 
def clean():     
    os.system("docker rm -f systemapi")     
    os.system("docker rmi systemapi")  

if __name__ == "__main__":          
    app()