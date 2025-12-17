import { createI18n } from 'vue-i18n'

const loadLocaleMessages = async () => {
  const modules = import.meta.glob('@/**/**/**/**/locales/*.json', { eager: true });
  return Object.entries(modules).reduce((messages, [path, module]) => {
    const parts = path.split('/');
    const domain = parts[3];
    const serviceArea = parts[4];
    const businessArea = parts[5];
    const langFile = parts[7];
    const language = langFile.split('.')[0];
    if (!messages[language]) messages[language] = {};
    if (!messages[language][domain]) messages[language][domain] = {};
    if (!messages[language][domain][serviceArea]) messages[language][domain][serviceArea] = {};
    messages[language][domain][serviceArea][businessArea] = (module as any).default;
    return messages;
  }, {} as any);
};

export const i18n = createI18n({
  legacy: false,
  locale: 'zh',
  fallbackLocale: 'en',
  messages: await loadLocaleMessages()
})
