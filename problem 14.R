#p 14

i<-0
collatz<- function (x) {
   while (x>1){
          i<-i+1
          
    if (x %% 2 == 0) {
    x<-x/2
  } else {
    x<-3*x+1
  }
          
   }
  return(i)
}

#je treba vymyslet, ktery cisla muzes rovnou poslat do prdele - napr ty pod 500K budou mit dycky o jeden krok
#min, nez jejich dvojnasobky
results<-matrix(nrow=1000000,ncol=1)
profvis{
  for (j in 500000:1000000){
    i<-1
    results[j,1]<-collatz(j)
    print(j)
  }
}

which.max(results)