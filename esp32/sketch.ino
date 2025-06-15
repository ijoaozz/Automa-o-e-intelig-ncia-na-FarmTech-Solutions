#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

// ANTIGO - const int SENSOR_UMIDADE_PIN = 34;
// ANTIGO - const int LED_STATUS_PIN = 2;
const uint8_t SENSOR_UMIDADE_PIN = 34;
const uint8_t LED_STATUS_PIN = 2;

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
  // 'valorPotenciometro': VALORES DE 0 a 4095.
  uint16_t valorPotenciometro = analogRead(SENSOR_UMIDADE_PIN); // OTIMIZAÇÃO: de int (4 bytes) para uint16_t (2 bytes)

  // 'umidadePercentual': VALORES DE 0 a 100.
  // 'uint8_t' (1 byte) IDEIAL!
  // ANTIGO: int umidadePercentual = map(valorPotenciometro, 0, 4095, 0, 100);
  uint8_t umidadePercentual = map(valorPotenciometro, 0, 4095, 0, 100); // OTIMIZAÇÃO: de int (4 bytes) para uint8_t (1 byte)

  Serial.print("Potenciometro: ");
  Serial.print(valorPotenciometro);
  Serial.print(" | Umidade (%): ");
  // APENAS o número para o Serial Plotter funcionar melhor
  Serial.println(umidadePercentual); // LINHA UTILIZADA PELO SERIAL PLOTTER

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
