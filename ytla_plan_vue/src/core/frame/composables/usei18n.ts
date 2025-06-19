import { createI18n } from 'vue-i18n'

const loadLocaleMessages = async () => {
  const modules = import.meta.glob('@/**/**/locales/*.json', { eager: true });

  return Object.entries(modules).reduce((messages, [path, module]) => {
    const parts = path.split('/');
    const feature = parts[3];
    const langFile = parts[5];
    const language = langFile.split('.')[0];

    if (!messages[language]) messages[language] = {};
    messages[language][feature] = (module as any).default;
    return messages;
  }, {} as any);
};

export const i18n = createI18n({
  legacy: false,
  locale: 'zh',
  fallbackLocale: 'en',
  messages: await loadLocaleMessages()
})
