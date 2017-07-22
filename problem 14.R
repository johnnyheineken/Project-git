#p 14

collatz<- function (x) {
   i<-0
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
profvis({
  for (j in setdiff((500001:1000000),3*seq(166665,333333,2)+1)){
    i<-1
    results[j,1]<-collatz(j)
  }
}
)


print(paste('the answer is',which.max(results)))

###testing###
i<-0
collatz1<- function (x) {
  while (x>1){
    i<-i+1
    
    if (x/2 == round(x/2)) {
      x<-x/2
    } else {
      x<-(3*x)+1
    }
  
  }
  return(i)
}

#je treba vymyslet, ktery cisla muzes rovnou poslat do prdele - napr ty pod 500K budou mit dycky o jeden krok
#min, nez jejich dvojnasobky
results<-matrix(nrow=1000000,ncol=1)
profvis(
  for (j in setdiff((500001:1000000),3*seq(166666,333333,2)+1)){
    i<-1
    results[j,1]<-collatz1(j)
  }
)


print(paste('the answer is',which.max(results)))

###testing second try###
collatz2<- function (j) {
  i=1
  x<-j
  while (x>1 && !(x %in% known_numbers)){
    return(x)
    if (x %% 2 == 0) {
        x<-x/2
        i<-i+1
      
    } else {
      x<-3*x+1
      i=i+1
    }
    
  }
}


known_numbers<-matrix(nrow=10,ncol=1000)

for (j in setdiff((10:1),3*seq(166665,333333,2)+1)){
  known_numbers[j,i]<-collatz2(j)
}

sumy<-c(rep(x = NA,1000000))
for(i in 500000:1000000){
sumy[i]<-sum(!is.na(known_numbers[i,]))
}

known_numbers[1000000,]
max(sumy,na.rm = TRUE)

