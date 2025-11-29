import os
import random
import igraph as ig
import matplotlib.pyplot as plt

random.seed(42)

os.makedirs("mysolution", exist_ok=True)

# 2.
g = ig.Graph.Erdos_Renyi(n=100, p=0.05)

# 3.
print('\n\n ### Zadanie 3 ###')
print(g.summary())
print("Czy ważony:", g.es["weight"] if "weight" in g.es.attributes() else False)

# 4.
print('\n\n ### Zadanie 4 ###')
print("\nWęzły:")
print(list(range(100)))
print("\nKrawędzie:")
print(g.get_edgelist())

# 5.
weights = [round(random.uniform(0.01, 1), 4) for _ in range(g.ecount())]
g.es["weight"] = weights

# 6. 
print('\n\n ### Zadanie 6 ###')
print(g.summary())
print("Czy ważony:", "weight" in g.es.attributes())

# 7.
print('\n\n ### Zadanie 7 ###')
deg = g.degree()
print("\nStopnie:")
for i, d in enumerate(deg):
    print(i, d)

plt.figure(figsize=(7,4))
plt.hist(deg)
plt.title("Histogram stopni")
plt.xlabel("Stopień")
plt.ylabel("Liczba węzłów")
plt.tight_layout()
plt.savefig("mysolution/degree_histogram.png")
plt.close()
print("Zapisano: degree_histogram.png")

# 8.
print('\n\n ### Zadanie 8 ###')
components = g.components()
print("\nLiczba komponentów:", len(components))

# 9.
print('\n\n ### Zadanie 9 ###')
pagerank_values = g.pagerank(weights='weight')
vertex_sizes = [v * 500 for v in pagerank_values]
layout = g.layout("fr")

visual_style = {
    "vertex_size": vertex_sizes,
    "layout": layout,
    "bbox": (800, 800),
}

ig.plot(g, "mysolution/graph_pagerank.png", **visual_style)
print("Zapisano: graph_pagerank.png")