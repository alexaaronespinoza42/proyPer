package es.codegym.telegrambot;

import org.telegram.telegrambots.meta.TelegramBotsApi;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;
import org.telegram.telegrambots.updatesreceivers.DefaultBotSession;

import java.util.Map;

import static es.codegym.telegrambot.TelegramBotContent.*;

public class MyFirstTelegramBot extends MultiSessionTelegramBot {

    public static final String NAME = "NoahDrakoBot_bot";
    public static final String TOKEN = "6490648423:AAFC-iyN_B9szZiwAnhvtunCLsdO54hXW6w";

    public MyFirstTelegramBot() {
        super(NAME, TOKEN);
    }

    @Override
    public void onUpdateEventReceived(Update update) {
        // TODO: escribiremos la funcionalidad principal del bot aquí

        if (getMessageText().equals("/start")){
            setUserGlory(0);
            sendPhotoMessageAsync("step_1_pic");
            sendTextMessageAsync(STEP_1_TEXT,
                    Map.of("Hackear la nevera", "step_1_btn"));
        }

        if (getCallbackQueryButtonKey().equals("step_1_btn")){
            addUserGlory(20);
            sendPhotoMessageAsync("step_2_pic");
            sendTextMessageAsync(STEP_2_TEXT,
                    Map.of("Tomar una salchicha! +20 de fama","step_2_btn",
                            "Tomar un pescado! +20 de fama","step_2_btn",
                            "Tirar una lata de pepinillos! +20 de fama","step_2_btn"));
        }

        if (getCallbackQueryButtonKey().equals("step_2_btn")){
            setUserGlory(20);
            sendPhotoMessageAsync("step_3_pic");
            sendTextMessageAsync(STEP_3_TEXT,
                    Map.of("Hackear al robot aspiradora","step_3_btn"));}

        if (getCallbackQueryButtonKey().equals("step_3_btn")){
            addUserGlory(30);
            sendPhotoMessageAsync("step_4_pic");

            sendTextMessageAsync(STEP_4_TEXT,
                    Map.of("Enviar al robot a por comida! +30 de fama","step_4_btn",
                            "Dar un paseo con el robot! +30 de fama","step_4_btn",
                            "Huir del robot! +30 de fama","step_4_btn"));}

        if (getCallbackQueryButtonKey().equals("step_4_btn")){
            setUserGlory(40);
            sendPhotoMessageAsync("step_5_pic");
            sendTextMessageAsync(STEP_5_TEXT,
                    Map.of("Poner y escender goPro","step_5_btn"));}

        if (getCallbackQueryButtonKey().equals("step_5_btn")){
            addUserGlory(40);
            sendPhotoMessageAsync("step_6_pic");
            sendTextMessageAsync(STEP_6_TEXT,
                    Map.of("Usar la goPro! +40 de fama","step_6_btn",
                    "Romper la goPro! +40 de fama","step_6_btn",
                    "Hackear la goPro! +40 de fama","step_6_btn"));
        }

        if (getCallbackQueryButtonKey().equals("step_6_btn")){
            setUserGlory(50);
            sendPhotoMessageAsync("step_7_pic");
            sendTextMessageAsync(STEP_7_TEXT,
                    Map.of("Hackear contraseña","step_7_btn"));
        }

        if (getCallbackQueryButtonKey().equals("step_7_btn")){
            addUserGlory(50);
            sendPhotoMessageAsync("step_8_pic");
            sendTextMessageAsync(STEP_8_TEXT,
                    Map.of("Usar la computadora! +50 de fama","step_8_btn",
                            "Romper la computadora! +50 de fama","step_8_btn",
                            "Meterle virus a la computadora! +50 de fama","step_8_btn"));
        }

        if (getCallbackQueryButtonKey().equals("step_8_btn")){
            setUserGlory(60);
            sendPhotoMessageAsync("final_pic");
            sendTextMessageAsync(FINAL_TEXT,
                    Map.of("Despidete !","step_9_btn"));
        }
        if (getCallbackQueryButtonKey().equals("step_9_btn")){
            addUserGlory(60);
            sendTextMessageAsync(FINAL_TEXT2);
        }
    }

    public static void main(String[] args) throws TelegramApiException {
        TelegramBotsApi telegramBotsApi = new TelegramBotsApi(DefaultBotSession.class);
        telegramBotsApi.registerBot(new MyFirstTelegramBot());
    }
}