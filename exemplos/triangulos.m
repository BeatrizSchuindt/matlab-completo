% Classificação de Triângulos
% Objetivo: Testar expressões lógicas e estruturas condicionais aninhadas.

a = input('Informe o lado a: ');
b = input('Informe o lado b: ');
c = input('Informe o lado c: ');

% Verificação de valores positivos
if (a <= 0 || b <= 0 || c <= 0)
  error('Medidas inválidas');
end

% Verificação de existência do triângulo
if (a + b <= c || a + c <= b || b + c <= a)
  error('Medidas inválidas');
end

% Classificação do triângulo
if (a == b && b == c)
  fprintf('Triângulo equilátero válido\n');
elseif (a == b || a == c || b == c)
  fprintf('Triângulo isósceles válido\n');
else
  fprintf('Triângulo escaleno válido\n');
end
