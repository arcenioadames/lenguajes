package modelo
type stack []string

func (s stack) push(v string) stack {
    return append(s, v)
}

func (s stack) pop() (stack, string) {
    l := len(s)
    return s[:l-1], s[l-1]
}

func main() {
    // Definir la gramática y construir la tabla de análisis sintáctico
    // ...

    // Definir la entrada a analizar
    input := "a + b * c"

    // Convertir la entrada en una lista de tokens
    tokens := strings.Split(input, " ")

    // Empujar el token de fin de cadena ($) y el símbolo inicial en la pila
    stack := stack{"$", "<expr>"}

    // Analizar sintácticamente la entrada
    for len(stack) > 0 {
        // Leer el primer símbolo de la pila de análisis
        symbol := stack[len(stack)-1]

        // Si el símbolo es un terminal, compararlo con el primer token de entrada
        if isTerminal(symbol) {
            if symbol == tokens[0] {
                // El terminal coincide con el token de entrada
                stack, tokens = stack.pop()
                tokens = tokens[1:]
            } else {
                // Se trata de un error sintáctico
                fmt.Println("Error sintáctico")
                return
            }
        } else {
            // El símbolo es un no terminal, buscar la
