import { createI18n } from 'vue-i18n'

const loadLocaleMessages = async () => {
  const modules = import.meta.glob('@/**/**/**/**/locales/*.json', { eager: true });
  return Object.entries(modules).reduce((messages, [path, module]) => {
    const parts = path.split('/');
    const type = parts[3];
    const area = parts[4];
    const subType = parts[5];
    const langFile = parts[7];
    const language = langFile.split('.')[0];
    if (!messages[language]) messages[language] = {};
    if (!messages[language][type]) messages[language][type] = {};
    messages[language][type][subType] = (module as any).default;
    return messages;
  }, {} as any);
};

export const i18n = createI18n({
  legacy: false,
  locale: 'zh',
  fallbackLocale: 'en',
  messages: await loadLocaleMessages()
})
