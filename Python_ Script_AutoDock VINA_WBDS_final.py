#Python Script para correr AutoDock VINA
#Date: 3/2023

from vina import Vina 
import os
import pandas as pd
from datetime import datetime

#%% SETEO DE PARÁMETROS DEL DOCKING (MODIFICAR SÓLO LO QUE ESTA EN ANARANJADO O BLANCO)

Receptor = "/home/virginia/Escritorio/Doctorado/LideB/Docking/Tutorial/Archivos/Archivos_para_Dockear/Receptor/1iep_conH_final.pdbqt"

Ligandos = "/home/virginia/Escritorio/Doctorado/LideB/Docking/Tutorial/Archivos/Archivos_para_Dockear/Ligando"
#Carpetas donde tenemos guardados los ligandos a Dockear

Observaciones = "" #Observaciónes importantes para el readme_file

Center =[14, 98, 57]
Box_size=[25, 25, 25]
Exhaustiveness = 64
N_poses = 10
Campo_fuerzas = 'vina'      #Si se desea usar otro campo de fuerzas como ad4 o vinardo cambiar la palabra vina por el campo deseado

output_file = "/home/virginia/Escritorio/Doctorado/LideB/Docking/Tutorial/Resultados_Docking/output_file.txt"
readme_file = "/home/virginia/Escritorio/Doctorado/LideB/Docking/Tutorial/Resultados_Docking/readme_file.txt"

hoy = datetime.today()
Fecha = hoy.strftime("%d/%m/%Y %H:%M:%S")
Ligandos_carpeta= os.listdir(Ligandos) 


#%% CORRIDA 

v = Vina(sf_name= Campo_fuerzas)    #Crea el objeto Vina. sf_name especifica el campo de fuerzas que va a usar.

v.set_receptor(Receptor)    #Carga del archivo del receptor. 

v.compute_vina_maps(center= Center,box_size=Box_size) #Computar los affinity maps para cada ligando

output = []
for ligando in Ligandos_carpeta:
    
    if ligando.endswith(".pdbqt"): 
        # Selección de ligandos de la carpeta especificada
        v.set_ligand_from_file(f'{Ligandos}/{ligando}')
        # Docking del ligando
        v.dock(exhaustiveness= Exhaustiveness, n_poses= N_poses)
        # Escritura la pose
        v.write_poses(pdbqt_filename=f"/home/virginia/Escritorio/Doctorado/LideB/Docking/Tutorial/Resultados_Docking/Resultados_{ligando}", n_poses= N_poses, overwrite=True)
        # Escritura output pose-score
        energies = v.energies()
        score = (ligando, energies[0,0])
        output.append(score)


#%% ESCRITURA DE OUTPUT FILES  

final = pd.DataFrame(output)
final = final.rename(columns={0:'Ligando', 1:'TOP SCORE'})
final.to_csv(output_file, sep=',', header=True, index=False, mode='w')
  

with open(readme_file,"w") as f:
    f.write("PROTOCOLO DE DOCKING:" + "\n")
    f.write("Fecha:" + Fecha + "\n" + "\n")
    f.write("Observaciones:" + Observaciones + "\n" + "\n")
    
    
    f.write("Configuración:" + "\n")
    f.write("Receptor:" + Receptor + "\n")
    f.write("Ligandos:" + Ligandos + "\n")
    f.write("Grilla:  CENTRO " + str(Center) + "  TAMAÑO " + str(Box_size) + "\n" + "\n")
    
    f.write("Parámetros usados:" + "\n")
    f.write("Campo de fuerzas:" + Campo_fuerzas + "\n")
    f.write("Exhaustiveness:" + str(Exhaustiveness) + "\n")
    f.write("Número de poses:" + str(N_poses) + "\n" + "\n")
     
    f.write("Archivo output:" + output_file + "\n")
    f.write("Archivo readme:" + readme_file + "\n")
