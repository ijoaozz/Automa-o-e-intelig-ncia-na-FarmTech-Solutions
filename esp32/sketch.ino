#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

// Otimização: Pinos são números pequenos (0-255), 'uint8_t' (1 byte) é suficiente.
// Antes: const int SENSOR_UMIDADE_PIN = 34;
// Antes: const int LED_STATUS_PIN = 2;
const uint8_t SENSOR_UMIDADE_PIN = 34; // Otimizado: de int (4 bytes) para uint8_t (1 byte)
const uint8_t LED_STATUS_PIN = 2;       // Otimizado: de int (4 bytes) para uint8_t (1 byte)

void setup() {
  Serial.begin(115200);
  pinMode(LED_STATUS_PIN, OUTPUT);

  lcd.init();
  lcd.backlight();

  lcd.print("FarmTech v1.0");
  lcd.setCursor(0, 1);
  lcd.print("Iniciando...");
  delay(2000);
  lcd.clear();
}

void loop() {
  // 'valorPotenciometro': Valores de 0 a 4095.
  // 'uint16_t' (2 bytes) é o ideal, pois 'int' (4 bytes) seria um desperdício.
  // Se não fosse usar para mapeamento, poderíamos até usar 'int' e não se preocupar tanto.
  // Mas para fins de demonstração de otimização, vamos usar o tipo mais adequado.
  uint16_t valorPotenciometro = analogRead(SENSOR_UMIDADE_PIN); // Otimizado: de int (4 bytes) para uint16_t (2 bytes)

  // 'umidadePercentual': Valores de 0 a 100.
  // 'uint8_t' (1 byte) é perfeito para isso!
  // Antes: int umidadePercentual = map(valorPotenciometro, 0, 4095, 0, 100);
  uint8_t umidadePercentual = map(valorPotenciometro, 0, 4095, 0, 100); // Otimizado: de int (4 bytes) para uint8_t (1 byte)

  Serial.print("Potenciometro: ");
  Serial.print(valorPotenciometro);
  Serial.print(" | Umidade (%): ");
  // Para o Serial Plotter, enviaremos apenas o valor numérico puro.
  // NÃO coloque texto na mesma linha que o valor que deseja plotar.
  // Por isso, usaremos dois 'Serial.println' separados ou um 'Serial.print' e um 'Serial.println'.
  // Para o Serial Plotter funcionar bem, queremos APENAS o número.
  Serial.println(umidadePercentual); // Esta linha será usada pelo Serial Plotter

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Umidade: ");
  lcd.print(umidadePercentual);
  lcd.print("%");

  lcd.setCursor(0, 1);
  if (umidadePercentual < 30) {
    lcd.print("STATUS: Irrigar!");
    digitalWrite(LED_STATUS_PIN, HIGH);
  } else {
    lcd.print("STATUS: OK");
    digitalWrite(LED_STATUS_PIN, LOW);
  }

  delay(3000);
}