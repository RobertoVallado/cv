import yaml from 'js-yaml';
import { readFileSync } from 'fs';
import { resolve } from 'path';
export const prerender = true;
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => {
  const yamlText = readFileSync(resolve(process.cwd(), '..', 'resume.yml'), 'utf-8');
  const data = (yaml.load(yamlText) as any) || {};
  return { work: data.work || [] };
};
