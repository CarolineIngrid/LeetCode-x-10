function isNumber(s) {
    // Define a expressão regular para validar o número
    const regex = /^[+\-]?\d+(\.\d+)?([eE][+\-]?\d+)?$/;
  
    // Testa a string "s" com a expressão regular
    return regex.test(s.trim());
  }
  