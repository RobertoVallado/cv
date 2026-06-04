<script lang="ts">
  import { t } from '$lib/i18n';

  const normalizeUrl = (url: string) =>
    url ? url.replaceAll('https://','').replaceAll('http://','') : '';

  $: stats = $t('achievements.stats') as { stat: string; source: string }[];
  $: awardsList = $t('achievements.awards_list') as { award: string; issuer: string }[];
</script>

<svelte:head>
  <title>{$t('achievements.page_title')}</title>
</svelte:head>

<h2>{$t('achievements.h2')}</h2>

<h3>{$t('achievements.highlights')}</h3>
<ul class="stats">
  {#each stats as { stat, source }}
    <li>
      {stat}
      {#if source}
        <a class="source" href={source} target="_blank" rel="nofollow" title={`Source: ${normalizeUrl(source)}`}>
          <i class="fa-solid fa-link"></i>
        </a>
      {/if}
    </li>
  {/each}
</ul>

<hr>

<h3>{$t('achievements.awards')}</h3>
<ul class="awards">
  {#each awardsList as { award, issuer }}
    <li>{award} — <span class="issuer">{issuer}</span></li>
  {/each}
</ul>

<hr>

<p class="projects-more">
  {$t('achievements.footer')}
  <a href="https://github.com/RobertoVallado" target="_blank">{$t('achievements.github')}</a>
  {$t('achievements.or')}
  <a href="/contact">{$t('achievements.contact')}</a>.
</p>

<style lang="scss">
  h2 { font-size: 1.8rem; text-align: center; font-weight: 500; }
  h3 { margin: 1rem 0 0.5rem; }
  p, a, li, span, div { font-size: 0.9rem; }
  ul { margin: 0; padding-left: 1.5rem; }
  li { margin: 0.4rem 0; line-height: 1.5; }
  hr { margin: 1rem 0; opacity: 0.8; }
  .source { font-size: 0.65rem; opacity: 0.65; margin-left: 2px; &:hover { opacity: 1; } }
  .issuer { font-style: italic; opacity: 0.75; }
  .projects-more { opacity: 0.8; font-style: italic; font-size: 0.8rem; }
</style>
