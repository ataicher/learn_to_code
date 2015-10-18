% [mean std mean_error std_error] = sub_chains(N, iter=1000)
%
function [mean std varargout] = sub_chains(N,varargin)

% display 16 significant digits
format long

if N < 10
   % N! x N matrix with every permutation of 1,2,...N
   pMat = perms(1:N);
   iter = factorial(N);
else
  % get user input for number of iterations
  if length(varargin)
     iter = varargin{1};
  else
     iter = 1000;
     warning("using %d random permutations",iter)
  end
end

% initialize array to store M for each permutation and initialize mean
% and std
max_sub_chains = zeros(iter,1);
mean = 0;
std = 0;

% loop over permuations
for i = 1:iter
  if N < 10
    % grab a row from permutations matrix
    p = pMat(i,:);
  else
    % obtain a random permutation of 1:N every iteration
    p = randperm(N);
  end
  
  % determine the max number of subchains for permutation p
  Mat = bsxfun(@minus,p(1:end-2),p(2:end-1)');
  Mat = tril(abs(Mat) == 1);
  M = sum(sum(Mat,2) == 0) + 1;
  
  % store M and update mean and std
  max_sub_chains(i) = M;
  mean = mean + M;
  std = std + M^2;
end

mean = mean/iter;
std = sqrt(std/iter - mean^2);

% For N < 10 the mean and std obey the formulas:
%   mean = (N+1)/3
%   std = sqrt(2*(N+1)/45)
% so I calculate the error with these formulas for N >= 10 
if N >=  10
  varargout{1} = abs(mean - (N+1)/3);
  varargout{2} = abs(std - sqrt(2*(N+1)/45));;
end

% plot a histogram of showing how many permutations had M maximal
% number of sub-chains
hist(max_sub_chains,1:ceil(N/2))
xlabel("M")
ylabel("# of permutations")
title("histogram of M")
