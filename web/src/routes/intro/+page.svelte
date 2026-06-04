<script lang="ts">
  import { t } from '$lib/i18n';

  const paragraphKeys = ['intro.p0','intro.p1','intro.p2','intro.p3','intro.p4','intro.p5'];

  const navLinks = [
    { key: 'nav.experience',   url: '/experience',   icon: 'fa-briefcase' },
    { key: 'nav.skills',       url: '/skills',       icon: 'fa-code' },
    { key: 'nav.achievements', url: '/achievements', icon: 'fa-star' },
    { key: 'nav.contact',      url: '/contact',      icon: 'fa-paper-plane' },
  ];
</script>

<svelte:head>
  <title>{$t('intro.page_title')}</title>
</svelte:head>

<h1>{$t('intro.h1')}</h1>
<h2>{$t('intro.greeting')}</h2>
<p class="tagline">{$t('intro.tagline')}</p>

{#each paragraphKeys as key}
  <p>{$t(key)}</p>
{/each}

<div class="other-pages">
  {#each navLinks as { key, url, icon }}
    <a href={url} class="no-underline">
      <button class="big-btn"><i class="fa-solid {icon}"></i>{$t(key)}</button>
    </a>
  {/each}
</div>

<style lang="scss">
h1 { margin-bottom: 1rem; }
h2 { margin: 0; font-size: 1.5rem; }
.tagline {
  font-style: italic;
  opacity: 0.75;
  margin: 0.25rem 0 0.75rem;
  font-size: 0.95rem;
}
p { margin: 0.5rem 0; line-height: 1.6; }
.other-pages {
  margin-top: 1.5rem;
  display: grid;
  align-items: center;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 1rem;
  a button { margin: 0; font-size: 1rem; padding: 0.5rem; }
}
</style>
