import time
import subprocess
import matplotlib.pyplot as plt
import sys

def cyk_parser(tokens, grammar):
    n = len(tokens)
    if n == 0: return False
    table = [[set() for _ in range(n - l + 1)] for l in range(1, n + 1)]
    for i in range(n):
        for lhs, rhs_list in grammar.items():
            for rhs in rhs_list:
                if len(rhs) == 1 and rhs[0] == "num":
                    table[0][i].add(lhs)
    for l in range(2, n + 1):
        for s in range(n - l + 1):
            for p in range(1, l):
                for lhs, rhs_list in grammar.items():
                    for rhs in rhs_list:
                        if len(rhs) == 2:
                            B, C = rhs
                            if B in table[p-1][s] and C in table[l-p-1][s+p]:
                                table[l-1][s].add(lhs)
    return "E" in table[n-1][0]

grammar = {"E": [["E", "P"], ["num"]], "P": [["A", "E"]], "A": [["+"]]}

def main():
    # TAMAÑOS OPTIMIZADOS: Suficientes para ver la curva sin esperar minutos
    tamanos = [20, 100, 300, 500, 800] 
    tiempos_bison = []
    tiempos_cyk = []

    print(f"\n{'LONGITUD':<15} {'BISON (ms)':<15} {'CYK (ms)':<15}")
    print("-" * 45)

    try:
        for n in tamanos:
            expresion = " + ".join(["10"] * n)
            
            # 1. Medir Bison (Asegúrate de haber compilado con: gcc lex.yy.c parser.tab.c -o bison_parser)
            res = subprocess.run(['./bison_parser'], input=expresion, capture_output=True, text=True)
            t_bison = float(res.stdout) if res.stdout else 0.0
            
            # 2. Medir CYK
            tokens_cyk = ["num", "+"] * (n - 1) + ["num"]
            start = time.perf_counter()
            cyk_parser(tokens_cyk, grammar)
            t_cyk = (time.perf_counter() - start) * 1000
            
            tiempos_bison.append(t_bison)
            tiempos_cyk.append(t_cyk)
            
            print(f"{len(tokens_cyk):<15} {t_bison:<15.4f} {t_cyk:<15.4f}")


        plt.figure(figsize=(10, 6))
        plt.yscale('log') # Escala logarítmica para ver ambas curvas
        plt.plot(tamanos, tiempos_cyk, 'r-o', linewidth=2, label='Algoritmo CYK O(n^3)')
        plt.plot(tamanos, tiempos_bison, 'b-s', linewidth=2, label='Bison LALR O(n)')
        
        plt.title('Comparativa de Rendimiento: Análisis Sintáctico')
        plt.xlabel('Número de Elementos en la Expresión')
        plt.ylabel('Tiempo de Ejecución (ms) - ESCALA LOG')
        plt.legend()
        plt.grid(True, which="both", ls="--", alpha=0.4)

        # GUARDAR AUTOMÁTICAMENTE
        plt.savefig('grafica_final.png')
        
        # Mostrar en pantalla
        plt.show()

    except KeyboardInterrupt:
        print("Prueba cancelada")
        sys.exit(0)

if __name__ == "__main__":
    main()