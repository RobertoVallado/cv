import { writable, derived } from 'svelte/store';
import { browser } from '$app/environment';

import en from './locales/en.json';
import fr from './locales/fr.json';

export const LOCALES = ['en', 'fr'] as const;
export type Locale = typeof LOCALES[number];

const messages: Record<Locale, Record<string, any>> = { en, fr };

function getStored(): Locale {
  if (!browser) return 'en';
  const s = localStorage.getItem('locale');
  return (s === 'en' || s === 'fr') ? s : 'en';
}

export const locale = writable<Locale>(getStored());

locale.subscribe(l => {
  if (browser) localStorage.setItem('locale', l);
});

export function setLocale(l: Locale) {
  locale.set(l);
}

// $t('some.nested.key') — falls back to English if key missing in active locale
export const t = derived(locale, $l => {
  return (key: string): any => {
    const keys = key.split('.');
    const resolve = (obj: any) => keys.reduce((v, k) => v?.[k], obj);
    return resolve(messages[$l]) ?? resolve(messages.en) ?? key;
  };
});
