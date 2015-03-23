library(tidyr)
library(dplyr)
library(ggplot2)

BogotaURL <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_14_0/station.txt"
CaliURL <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_14_0/station.txt"
BucaramangaURL <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_14_0/station.txt"
BarranquillaURL <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_14_0/station.txt"
IpialesURL <- "http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_14_0/station.txt"

download.file(BogotaURL,destfile = 'bog.txt', method ='curl')
download.file(CaliURL,destfile = 'cal.txt', method ='curl')
download.file(BucaramangaURL,destfile = 'buc.txt', method ='curl')
download.file(BarranquillaURL,destfile = 'bar.txt', method ='curl')
download.file(IpialesURL,destfile = 'ipi.txt', method ='curl')

bog <- read.table('bog.txt',header=T)
cal <- read.table('cal.txt',header=T)
buc <- read.table('buc.txt',header=T)
bar <- read.table('bar.txt',header=T)
ipi <- read.table('ipi.txt',header=T)

bog <- bog %>% gather(MONTH, TEMPERATURE,-YEAR)
cal <- cal %>% gather(MONTH, TEMPERATURE,-YEAR)
buc <- buc %>% gather(MONTH, TEMPERATURE,-YEAR)
bar <- bar %>% gather(MONTH, TEMPERATURE,-YEAR)
ipi <- ipi %>% gather(MONTH, TEMPERATURE,-YEAR)

bog <- subset(bog,bog$TEMPERATURE < 900)
cal <- subset(cal,cal$TEMPERATURE < 900)
buc <- subset(buc,buc$TEMPERATURE < 900)
bar <- subset(bar,bar$TEMPERATURE < 900)
ipi <- subset(ipi,ipi$TEMPERATURE < 900)

bog["CITY"] <- "Bogota"
cal["CITY"] <- "Cali"
buc["CITY"] <- "Bucaramanga"
bar["CITY"] <- "Barranquilla"
ipi["CITY"] <- "Ipiales"

bog <- subset(bog,bog$MONTH == "JAN" | bog$MONTH == "FEB" | bog$MONTH == "MAR" | bog$MONTH == "APR" | bog$MONTH == "MAY" | bog$MONTH == "JUN" | bog$MONTH == "JUL" | bog$MONTH == "AUG" | bog$MONTH == "SEP" | bog$MONTH == "OCT" | bog$MONTH == "NOV" | bog$MONTH == "DEC")
cal <- subset(cal,cal$MONTH == "JAN" | cal$MONTH == "FEB" | cal$MONTH == "MAR" | cal$MONTH == "APR" | cal$MONTH == "MAY" | cal$MONTH == "JUN" | cal$MONTH == "JUL" | cal$MONTH == "AUG" | cal$MONTH == "SEP" | cal$MONTH == "OCT" | cal$MONTH == "NOV" | cal$MONTH == "DEC")
buc <- subset(buc,buc$MONTH == "JAN" | buc$MONTH == "FEB" | buc$MONTH == "MAR" | buc$MONTH == "APR" | buc$MONTH == "MAY" | buc$MONTH == "JUN" | buc$MONTH == "JUL" | buc$MONTH == "AUG" | buc$MONTH == "SEP" | buc$MONTH == "OCT" | buc$MONTH == "NOV" | buc$MONTH == "DEC")
bar <- subset(bar,bar$MONTH == "JAN" | bar$MONTH == "FEB" | bar$MONTH == "MAR" | bar$MONTH == "APR" | bar$MONTH == "MAY" | bar$MONTH == "JUN" | bar$MONTH == "JUL" | bar$MONTH == "AUG" | bar$MONTH == "SEP" | bar$MONTH == "OCT" | bar$MONTH == "NOV" | bar$MONTH == "DEC")
ipi <- subset(ipi,ipi$MONTH == "JAN" | ipi$MONTH == "FEB" | ipi$MONTH == "MAR" | ipi$MONTH == "APR" | ipi$MONTH == "MAY" | ipi$MONTH == "JUN" | ipi$MONTH == "JUL" | ipi$MONTH == "AUG" | ipi$MONTH == "SEP" | ipi$MONTH == "OCT" | ipi$MONTH == "NOV" | ipi$MONTH == "DEC")

df <- rbind(bog,cal,buc,bar,ipi)
df <- rename(df,anio=YEAR,mes=MONTH,temperatura=TEMPERATURE,ciudad=CITY)
df$mes <- match(df$mes, toupper(month.abb))
df$fecha <- with(df,ISOdate(anio, mes, 1))
write.table(df, file = "Calentamientoglobal.csv", sep= ",",row.names=F)

ggplot(df, aes(x = fecha, y = temperatura, color = ciudad)) + geom_point(size=1) + geom_line() + ylab("Temperatura °C") + xlab("Fecha") + facet_wrap(~ciudad, scales="free_y") + ggsave(file="graph.png", width=49, height=15)

