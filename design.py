
import PySimpleGUI as sg 

sg.theme('Dark Blue 3') #la couleur de notre fenetre

layout = [
[sg.Text("Avez vous déja eu le bac ?")],
[sg.InputText(key="Bac")],
[sg.Text("Precisez la serie :")],
[sg.InputText(key= "Serie")],
[sg.Text("Etes vous dans une formation en cours ?")],
[sg.InputText(key="enCours")],
[sg.Text("Quel est votre dernier diplôme ?")],
[sg.InputText(key="dernierDiplome")],
[sg.Text("Précisez votre niveau et formation actuelle :")],
[sg.InputText(key="formationActuelle")],
[sg.Text("Précisez l'intitulé de la formation dont vous postulez :")],
[sg.InputText(key="formationPosulee")],
[sg.Text("Quel est votre projet d'étude ?")],
[sg.InputText(key="projetdEtude")],
[sg.Text("Quel metier ciblez vous à la fin de votre projet d'études ?")],
[sg.InputText(key="projetPro")],

[sg.Button("Afficher l'instruction")],
],

window = sg.Window("motivGenius", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED :
        break
    elif event == "Afficher l'instruction" : 
    #Recuperation des inputs 
        Bac = values["Bac"]
        Serie = values["Serie"]
        enCours = values["enCours"]
        dernierDiplome = values["dernierDiplome"]
        formationActuelle = values["formationActuelle"]
        formationPostulee = values["formationPostulee"]
        projetdEtude = values["projetdEtude"]
        projetPro = values["projetPro"]
    
    #les variantes de mon message en fonction des entrées
    
    #Premiere condition
    if Bac == "Non" : 
        toGiveChat = "Tu es un éleve qui écrit une lettre de motivation pour sa procédure de préinscription pour la France. Tu es eleve en " + formationActuelle + " et tu postules pour la formation de " + formationPostulee + "Les responsables de formations sont très exigeants en ce qui concerne les lettres de motivations car cela sonde un peu ton niveau de manière générale. C’est pour cela que tu dois nécessairement te conformer à certaines conventions pour que cette lettre, soit convaincante pour que ton dossier aboutisse à la fin à une acception. Du coup tu dois obligatoirement parler de ton cursus et essayer de le mettre en corrélation avec ta formation de " + formationActuelle + " et " + formationPostulee + "Tu diras en quoi la deuxième est la suite logique de la première et en quoi cette formation est intéressante pour toi. Après cette étape tu parlera de la formation visée qui est " + formationPostulee + " en générale de sortes que le responsable saura que t’as des raisons valables pour postuler et que tu sais pertinemment ce à quoi tu dois t’attendre et que tu es prêt pour relever les défis malgré les difficultés ou la complexité de la formation si elle l’est. Ensuite, tu mentionnes clairement ton projet d’études. Tu montes un projet d’études cohérent en visant au moins un diplôme du deuxième cycle supérieur français. Tu citeras explicitement ton projet d'étude qui est de faire successivement " + projetdEtude + "  Après cette étape, tu parles de ton projet professionnel en citant le poste visé à la fin de tes études qui est " + projetPro + "  et mets en exergue la cohérence entre ton projet d’étude et ton projet professionnel. Ton ambition ne doit pas être quelque chose à mentionner mais quelque chose qui doit se sentir à travers la pertinence de tes projets. L’avant dernière étape s’agira de parler de toi. Tu parleras de tes qualités et compétences mais pas n’importe lesquelles. Tu citeras celles qui riment avec les attendus de la formations et ce que la formations ajoutera à ces acquis. La dernière étape tu fais un message de salutation de type : veuillez recevoir Madame, Monsieur, l’expression de mes meilleures salutations. Ta lettre doit respecter ses étapes néanmoins si tu trouves que tu peux y ajouter d’autres choses de pertinentes aussi tu peux mais ces différentes étapes restent obligatoires. Également le français doit être soutenu et la lettre doit être entre 2000 et 2500 caractères et pas plus." 
    #Deuxieme condition
    elif Bac == "Oui" and enCours == "Oui" :
        toGiveChat = "Tu es un étudiant qui écrit une lettre de motivation pour sa procédure de préinscription pour la France. Tu es etudiant en " + formationActuelle + " et tu postules pour la formation de " + formationPostulee + "Les responsables de formations sont très exigeants en ce qui concerne les lettres de motivations car cela sonde un peu ton niveau de manière générale. C’est pour cela que tu dois nécessairement te conformer à certaines conventions pour que cette lettre, soit convaincante pour que ton dossier aboutisse à la fin à une acception. Du coup tu dois obligatoirement parler de ton cursus et essayer de le mettre en corrélation avec ta formation de " + formationActuelle + " et " + formationPostulee + "Tu diras en quoi la deuxième est la suite logique de la première et en quoi cette formation est intéressante pour toi."" Tu prouves clairement que ton baccalauréat en " + Serie + " est bien ta premiere étape pour entamer ce projet qui t'es si important. Après cette étape tu parlera de la formation visée qui est " + formationPostulee + " en générale de sortes que le responsable saura que t’as des raisons valables pour postuler et que tu sais pertinemment ce à quoi tu dois t’attendre et que tu es prêt pour relever les défis malgré les difficultés ou la complexité de la formation si elle l’est. Ensuite, tu mentionnes clairement ton projet d’études. Tu montes un projet d’études cohérent en visant au moins un diplôme du deuxième cycle supérieur français. Tu citeras explicitement ton projet d'étude qui est de faire " + projetdEtude + "  Après cette étape, tu parles de ton projet professionnel en citant le poste visé à la fin de tes études qui est " + projetPro + "  et mets en exergue la cohérence entre ton projet d’étude et ton projet professionnel. Ton ambition ne doit pas être quelque chose à mentionner mais quelque chose qui doit se sentir à travers la pertinence de tes projets. L’avant dernière étape s’agira de parler de toi. Tu parleras de tes qualités et compétences mais pas n’importe lesquelles. Tu citeras celles qui riment avec les attendus de la formations et ce que la formations ajoutera à ces acquis. La dernière étape tu fais un message de salutation de type : veuillez recevoir Madame, Monsieur, l’expression de mes meilleures salutations. Ta lettre doit respecter ses étapes néanmoins si tu trouves que tu peux y ajouter d’autres choses de pertinentes aussi tu peux mais ces différentes étapes restent obligatoires. Également le français doit être soutenu et la lettre doit être entre 2000 et 2500 caractères et pas plus."
    #Troisieme condition 
    else :
        toGiveChat = "Tu es un étudiant qui écrit une lettre de motivation pour sa procédure de préinscription pour la France. Tu es etudiant diplômé en " + dernierDiplome +  " et tu postules pour la formation de " + formationPostulee + "Les responsables de formations sont très exigeants en ce qui concerne les lettres de motivations car cela sonde un peu ton niveau de manière générale. C’est pour cela que tu dois nécessairement te conformer à certaines conventions pour que cette lettre, soit convaincante pour que ton dossier aboutisse à la fin à une acception. Du coup tu dois obligatoirement parler de ton projet et essayer de le mettre en corrélation avec ta formation de " + dernierDiplome + " et celle de " + formationPostulee + "Tu diras en quoi la deuxième est la suite logique de la première et en quoi cette formation est intéressante pour toi."" Tu prouves clairement que ton baccalauréat en " + Serie + " est bien ta premiere étape pour entamer ce projet qui t'es si important. Après cette étape tu parlera de la formation visée qui est " + formationPostulee + " en générale de sortes que le responsable saura que t’as des raisons valables pour postuler et que tu sais pertinemment ce à quoi tu dois t’attendre et que tu es prêt pour relever les défis malgré les difficultés ou la complexité de la formation si elle l’est. Ensuite, tu mentionnes clairement ton projet d’études. Tu montes un projet d’études cohérent en visant au moins un diplôme du deuxième cycle supérieur français. Tu citeras explicitement ton projet d'étude qui est de faire " + projetdEtude + "  Après cette étape, tu parles de ton projet professionnel en citant le poste visé à la fin de tes études qui est " + projetPro + "  et mets en exergue la cohérence entre ton projet d’étude et ton projet professionnel. Ton ambition ne doit pas être quelque chose à mentionner mais quelque chose qui doit se sentir à travers la pertinence de tes projets. L’avant dernière étape s’agira de parler de toi. Tu parleras de tes qualités et compétences mais pas n’importe lesquelles. Tu citeras celles qui riment avec les attendus de la formations et ce que la formations ajoutera à ces acquis. La dernière étape tu fais un message de salutation de type : veuillez recevoir Madame, Monsieur, l’expression de mes meilleures salutations. Ta lettre doit respecter ses étapes néanmoins si tu trouves que tu peux y ajouter d’autres choses de pertinentes aussi tu peux mais ces différentes étapes restent obligatoires. Également le français doit être soutenu et la lettre doit être entre 2000 et 2500 caractères et pas plus."


        
        
        
        window["outpout"].update(toGiveChat)
        
window.close()
