n = input('Digite o numero de linhas (n >= 1): ');

if n < 1
    fprintf('Erro: n deve ser um numero inteiro maior ou igual a 1.\n');
else
    row = [1];
    
    for i = 1:n
        for j = 1:i
            fprintf('%d', row(j));
            if j < i
                fprintf(' ');
            end
        end
        fprintf('\n');
        
        nextRow = zeros(1, i + 1);
        
        nextRow(1) = 1;
        nextRow(i + 1) = 1;
        
        for j = 2:i
            nextRow(j) = row(j - 1) + row(j);
        end
        
        row = nextRow;
    end
end
