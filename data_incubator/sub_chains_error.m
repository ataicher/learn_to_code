function sub_chains_error(N)

iter = [100 250 500 750 1000 2500 5000 7500 10000 25000 50000 75000 100000 200000];
n_iter = length(iter);

mean_error_vec = zeros(n_iter,1);
std_error_vec = zeros(n_iter,1);

for i = 1:n_iter
  [~, ~, mean_error, std_error] = sub_chains(N,iter(i));
  mean_error_vec(i) = mean_error;
  std_error_vec(i) = std_error;
end 

subplot(2,1,1)
semilogx(iter, mean_error_vec,'bx-')
subplot(2,1,2)
semilogx(iter, std_error_vec,'bx-')
