import yaml from 'js-yaml';
import { readFileSync } from 'fs';
import { resolve } from 'path';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = () => {
  const yamlText = readFileSync(resolve(process.cwd(), '..', 'resume.yml'), 'utf-8');
  const data = (yaml.load(yamlText) as any) || {};
  return { basics: data.basics || {} };
};
