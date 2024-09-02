def fibonacci(n):
    sequencia_fibonacci = [0, 1]  #
    while sequencia_fibonacci[-1] < n:  
        next_fib = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]  
        sequencia_fibonacci.append(next_fib)  
    return sequencia_fibonacci

def main():
  
    num = int(input("digite um número para verificar se pertence a sequencia:  "))
    
    sequencia_fibonacci = fibonacci(num)
    
    if num in sequencia_fibonacci:
        print(f"o número {num} pertence a sequência fibonacci.")
    else:
        print(f"o número {num} não pertence a sequência fibonacci.")

if __name__ == "__main__":
    main()
