function [mean std] = sub_chains(N,iter)

mean = 0;
std = 0;
for i = 1:iter
  p = randperm(N);
  Mat = bsxfun(@minus,repmat(p(1:end-2),N-2,1),p(2:end-1)');
  Mat = tril(abs(Mat) == 1);
  M = sum(sum(Mat,2) == 0);
  mean = mean + M;
  std = std + M*M;
end

mean = mean/iter;
std = sqrt(std/iter - mean^2);

  
