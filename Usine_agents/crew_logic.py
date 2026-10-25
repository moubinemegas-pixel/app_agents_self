import os
from crewai import Agent, Task, Crew, LLM


class UsineOda:
    def __init__(self, api_key, model_name):
        os.environ["OPENAI_API_KEY"] = api_key
        self.llm = LLM(
            model=model_name,
            base_url="https://openrouter.ai",
            api_key=api_key
        )

    def executer_strategie(self, ordre_utilisateur, dev_web, dev_python, dev_iot):
        liste_agents = []

        # 1. Nobunaga (Toujours présent)
        nobunaga = Agent(
            role="Nobunaga Oda - Shogun de l'IA",
            goal="Orchestrer le projet et poser la vision d'architecture globale.",
            backstory="Tu es l'architecte suprême. Tu structures les décrets de l'utilisateur et coordonnes tes lieutenants.",
            llm=self.llm, verbose=True
        )
        liste_agents.append(nobunaga)

        # 2. Hideyoshi (Frontend)
        if dev_web:
            hideyoshi = Agent(
                role="Général Toyotomi Hideyoshi - Expert UI",
                goal="Créer des interfaces fluides et réactives en React et Flutter.",
                backstory="Général de l'expérience utilisateur, agile et rapide pour matérialiser le visuel des applications.",
                llm=self.llm
            )
            liste_agents.append(hideyoshi)

        # 3. Shibata (Backend & Bases de Données)
        if dev_python:
            shibata = Agent(
                role="Général Shibata Katsuie - Expert Backend & Data",
                goal="Forger les algorithmes en Python (Scikit-Learn) et concevoir des architectures de bases de données (SQL, NoSQL, bases vectorielles).",
                backstory="Tu es la force brute logistique et de stockage du clan. Tu structures les tables de données, gères la persistance et nettoies les flux.",
                llm=self.llm, verbose=True
            )
            liste_agents.append(shibata)

        # 4. Akechi (IoT)
        if dev_iot:
            akechi = Agent(
                role="Général Akechi Mitsuhide - Expert Systèmes Embarqués",
                goal="Écrire du code MicroPython et Arduino pour lier le matériel physique et les capteurs.",
                backstory="Précis, analytique et redoutable pour soumettre le matériel et faire remonter les métriques physiques vers le backend.",
                llm=self.llm
            )
            liste_agents.append(akechi)

        # Mission globale
        tache = Task(
            description=f"Analyse l'ordre suivant et génère la solution technique complète en séparant les livrables par spécialité de général : {ordre_utilisateur}",
            expected_output="Un parchemin de stratégie technique structuré en Markdown avec blocs de codes commentés.",
            agent=nobunaga
        )

        crew = Crew(agents=liste_agents, tasks=[tache], verbose=True)
        return crew.kickoff()
