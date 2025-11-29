import igraph as ig

# 2.
g = ig.Graph.Barabasi(n=1000, m=2, directed=False)

# 3.
layout = g.layout("fr")
ig.plot(
    g,
    layout=layout,
    vertex_size=3,
    edge_width=0.2,
    bbox=(900, 900),
    margin=20,
    target="mysolution/ba_fr.png"
)

# 4.
bw = g.betweenness()
central = max(range(len(bw)), key=lambda i: bw[i])
print(f"Najbardziej centralny węzeł: {central}")

# 5.
print(f"Średnica grafu: {g.diameter()}")

# 6.
# - BA: mechanizm preferencyjnego przyłączania („bogaci się bogacą”).
# - BA: rozkład stopni ~ potęgowy, obecność hubów o bardzo dużym stopniu.
# - BA: struktura bardziej hierarchiczna, silnie zróżnicowane stopnie.
# - ER: każda para węzłów łączy się z tym samym prawdopodobieństwem p.
# - ER: rozkład stopni ~ Poissona, brak wyraźnych hubów.
# - ER: struktura bardziej jednorodna, stopnie skupione wokół średniej.
