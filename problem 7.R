#problem 7
#uz jsem to nejak rozbil zas

prime.numbers<-c(rep(0,10))
prime.numbers[1:3]<-c(2,3,5)
hodne<-150000

system.time(
profvis({
 

  for (i in seq(7,hodne,by=2)){
    if (0 %in% (i %%  prime.numbers[sqrt(i)>=prime.numbers])){
    } else {
     prime.numbers[sum(prime.numbers>0)+1]<-i
    }
  if (sum(prime.numbers>0)>10000){
    break
   }
  }

  })
)

tail(prime.numbers)

print(sum(prime.numbers))

print(prime.numbers[10001])
prime.numbers[10:101]

format(sum(prime.numbers),scientific=FALSE)
head(prime.numbers)
