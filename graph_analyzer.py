import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time

# ==============================================================================
# Fonctions de base pour la manipulation de graphes
# ==============================================================================

def create_graph(is_directed=False):
    """
    Crée un graphe (orienté ou non) en demandant à l'utilisateur
    le nombre de nœuds et les arêtes/arcs.
    """
    if is_directed:
        G = nx.DiGraph()
        edge_prompt = "Entrez un arc sous la forme 'source-destination' (ou 'stop') : "
    else:
        G = nx.Graph()
        edge_prompt = "Entrez une arête sous la forme 'noeud1-noeud2' (ou 'stop') : "

    while True:
        try:
            nombre_noeuds = int(input("Entrez le nombre de nœuds : "))
            if nombre_noeuds > 0:
                break
            print("Le nombre de nœuds doit être positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    
    G.add_nodes_from(range(1, nombre_noeuds + 1))
    print(f"Graphe avec {nombre_noeuds} nœuds créé. Ajoutez maintenant les liens.")

    while True:
        arc_input = input(edge_prompt)
        if arc_input.lower() == 'stop':
            break
        try:
            n1, n2 = map(int, arc_input.split('-'))
            if n1 > nombre_noeuds or n2 > nombre_noeuds or n1 <= 0 or n2 <= 0:
                print("Nœuds hors limites. Veuillez réessayer.")
                continue
            G.add_edge(n1, n2)
        except (ValueError, IndexError):
            print("Format invalide. Veuillez entrer un lien valide (ex: '1-2').")
            
    print("\n--- Graphe créé avec succès ---")
    return G

def show_graph(G):
    """Affiche le graphe donné en utilisant matplotlib."""
    if not G:
        print("Le graphe est vide. Veuillez d'abord en créer un.")
        return
    
    is_directed = isinstance(G, nx.DiGraph)
    pos = nx.spring_layout(G) # Pour une meilleure disposition
    
    if is_directed:
        nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=20, connectionstyle='arc3,rad=0.1', node_color='skyblue')
    else:
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightgreen')
    
    plt.show()

# ==============================================================================
# Fonctions d'analyse de graphes
# ==============================================================================

def calculate_density(G):
    if not G:
        print("Le graphe est vide.")
        return
    density = nx.density(G)
    print(f"Densité du graphe : {density:.4f}")

def calculate_degrees(G):
    if not G:
        print("Le graphe est vide.")
        return
    if not G.nodes():
        print("Le graphe n'a pas de nœuds.")
        return
    
    if isinstance(G, nx.DiGraph):
        in_deg = dict(G.in_degree())
        out_deg = dict(G.out_degree())
        print("Degrés entrants :", in_deg)
        print("Degrés sortants :", out_deg)
    else:
        degrees = dict(G.degree())
        print("Degrés des nœuds :", degrees)

def check_eulerian(G):
    if not G:
        print("Le graphe est vide.")
        return
    if nx.is_eulerian(G):
        print("Le graphe est eulérien.")
    else:
        print("Le graphe n'est pas eulérien.")

def check_complete(G):
    if not G:
        print("Le graphe est vide.")
        return
    # nx.is_complete n'existe pas, il faut le vérifier manuellement
    n = len(G.nodes())
    m = len(G.edges())
    if isinstance(G, nx.DiGraph):
        max_edges = n * (n - 1)
    else:
        max_edges = n * (n - 1) / 2
    
    if m == max_edges:
         print("Le graphe est complet.")
    else:
         print("Le graphe n'est pas complet.")


def check_tree(G):
    if not G:
        print("Le graphe est vide.")
        return
    if nx.is_tree(G):
        print("Le graphe est un arbre.")
    else:
        print("Le graphe n'est pas un arbre.")

def find_all_paths(G):
    if not G or len(G.nodes()) < 2:
        print("Le graphe est trop petit pour trouver des chemins.")
        return
    try:
        start_node = int(input("Entrez le nœud de départ : "))
        end_node = int(input("Entrez le nœud d'arrivée : "))
        if start_node not in G.nodes() or end_node not in G.nodes():
            print("Un des nœuds n'existe pas dans le graphe.")
            return

        paths = list(nx.all_simple_paths(G, source=start_node, target=end_node))
        if paths:
            print(f"Tous les chemins simples entre {start_node} et {end_node} :")
            for i, path in enumerate(paths):
                print(f"  Chemin {i+1}: {path}")
        else:
            print(f"Aucun chemin trouvé entre {start_node} et {end_node}.")
    except ValueError:
        print("Entrée invalide.")

def find_shortest_path(G):
    if not G or len(G.nodes()) < 2:
        print("Le graphe est trop petit pour trouver des chemins.")
        return
    try:
        start_node = int(input("Entrez le nœud de départ : "))
        end_node = int(input("Entrez le nœud d'arrivée : "))
        if start_node not in G.nodes() or end_node not in G.nodes():
            print("Un des nœuds n'existe pas dans le graphe.")
            return

        path = nx.shortest_path(G, source=start_node, target=end_node)
        print(f"Chemin le plus court entre {start_node} et {end_node} : {path}")
    except nx.NetworkXNoPath:
        print(f"Aucun chemin n'existe entre {start_node} et {end_node}.")
    except ValueError:
        print("Entrée invalide.")
        
def find_cycles(G):
    if not G:
        print("Le graphe est vide.")
        return
    cycles = list(nx.simple_cycles(G))
    if cycles:
        print("Cycles trouvés dans le graphe :")
        for i, cycle in enumerate(cycles):
            print(f"  Cycle {i+1}: {cycle}")
    else:
        print("Aucun cycle trouvé dans le graphe.")

# ==============================================================================
# Menu principal
# ==============================================================================

def print_menu():
    """Affiche le menu des options."""
    print("\n" + "="*50)
    print("Analyseur de Graphes - Menu Principal")
    print("="*50)
    print("1. Créer un nouveau graphe NON orienté")
    print("2. Créer un nouveau graphe ORIENTÉ")
    print("3. Afficher le graphe actuel")
    print("-" * 20)
    print("4. Calculer la densité")
    print("5. Calculer les degrés")
    print("6. Vérifier si le graphe est Eulérien")
    print("7. Vérifier si le graphe est Complet")
    print("8. Vérifier si le graphe est un Arbre")
    print("9. Trouver tous les chemins entre deux nœuds")
    print("10. Trouver le chemin le plus court entre deux nœuds")
    print("11. Trouver tous les cycles (pour graphes orientés)")
    print("-" * 20)
    print("0. Quitter")
    print("="*50)

def main():
    """Fonction principale qui gère le menu et les appels."""
    current_graph = None
    
    while True:
        print_menu()
        choice = input("Entrez votre choix : ")
        
        if choice == '1':
            current_graph = create_graph(is_directed=False)
            show_graph(current_graph)
        elif choice == '2':
            current_graph = create_graph(is_directed=True)
            show_graph(current_graph)
        elif choice == '3':
            show_graph(current_graph)
        elif choice == '4':
            calculate_density(current_graph)
        elif choice == '5':
            calculate_degrees(current_graph)
        elif choice == '6':
            check_eulerian(current_graph)
        elif choice == '7':
            check_complete(current_graph)
        elif choice == '8':
            check_tree(current_graph)
        elif choice == '9':
            find_all_paths(current_graph)
        elif choice == '10':
            find_shortest_path(current_graph)
        elif choice == '11':
            find_cycles(current_graph)
        elif choice == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()