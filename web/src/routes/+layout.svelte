<script lang="ts">
  import { browser } from '$app/environment';
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { onNavigate } from '$app/navigation';

  const SITE_URL = 'https://cv.robertovallado.dev';

  import '../app.css';
  import '../styles/variables.scss';
  import '../styles/link.scss';
  import '../styles/page-global.scss';

  import { t, locale, setLocale, LOCALES } from '$lib/i18n';

  export let data: { basics: any };

  interface Document {
    startViewTransition?: (callback: () => Promise<void>) => void;
  }

  onNavigate((navigation) => {
    const doc = document as Document;
    if (!doc.startViewTransition) return;
    return new Promise<void>((resolve) => {
      doc.startViewTransition && doc.startViewTransition(async () => {
        resolve();
        await navigation.complete;
      });
    });
  });

  let header: HTMLElement | null = null;
  let main: HTMLElement | null = null;

  function handleScroll() {
    if (header && main) {
      if (main.scrollTop > 60) {
        header.style.boxShadow = '0 4px 24px rgba(0, 0, 0, 0.4)';
        header.style.zIndex = '13';
      } else {
        header.style.boxShadow = '';
        header.style.zIndex = '';
      }
    }
  }

  onMount(() => {
    if (browser) {
      main?.addEventListener('scroll', handleScroll);
      return () => main?.removeEventListener('scroll', handleScroll);
    }
  });

  let path: string;
  // @ts-ignore
  $: path = $page.url.pathname;

  $: headline = $locale === 'fr' && data.basics['headline-fr']
    ? data.basics['headline-fr']
    : data.basics.headline;

  $: socials = [
    { name: 'GitHub',   url: data.basics.url,     icon: 'fa-github',   color: '#1A43BF' },
    { name: 'LinkedIn', url: data.basics.linkedin, icon: 'fa-linkedin', color: '#4A72C4' },
  ].filter(s => s.url);

  $: headerLinks = socials.map(({ name, url }) => ({ name, url }));

  $: canonical = SITE_URL + ($page.url.pathname.replace(/\/$/, '') || '/');

  $: jsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'Person',
    name: data.basics.name,
    jobTitle: data.basics.headline,
    email: data.basics.email,
    url: SITE_URL,
    sameAs: [data.basics.url, data.basics.linkedin].filter(Boolean),
    address: {
      '@type': 'PostalAddress',
      addressLocality: 'Québec',
      addressRegion: 'QC',
      addressCountry: 'CA',
    },
  });

  $: navLinks = [
    { key: 'nav.intro',        url: '/intro',        icon: 'fa-address-card' },
    { key: 'nav.experience',   url: '/experience',   icon: 'fa-briefcase' },
    { key: 'nav.achievements', url: '/achievements', icon: 'fa-star' },
    { key: 'nav.skills',       url: '/skills',       icon: 'fa-code' },
  ];
</script>

<svelte:head>
  <link rel="canonical" href={canonical}>
  {@html `<script type="application/ld+json">${jsonLd}</script>`}
</svelte:head>

<div class="app">
  <aside>
    <div class="aside-inner">
      <a href="/" class="no-underline"><h1>{data.basics.name}</h1></a>
      <p class="job-title">{headline}</p>
      <ul class="socials">
        {#each socials as { url, icon, color, name }}
          <li style="--hover-color: {color}">
            <a class="no-underline" href={url} target="_blank" rel="nofollow" aria-label={name}>
              <i class="fa-brands {icon}"></i>
            </a>
          </li>
        {/each}
      </ul>
      <nav class="cv-pages-nav">
        <ul>
          {#each navLinks as { key, url, icon }}
            <li class:is-active={path === url}>
              <a class="no-underline" href={url}>
                <i class="nav-icon fa-solid {icon}"></i>{$t(key)}
              </a>
            </li>
          {/each}
          {#if path !== '/'}
            <li>
              <a href="/" class="no-underline">
                <i class="nav-icon fa-solid fa-home"></i>{$t('nav.home')}
              </a>
            </li>
          {/if}
        </ul>
      </nav>
      <a href="/download" class="no-underline">
        <button class="download-btn">
          <i class="fa-solid fa-file-arrow-down"></i>{$t('nav.download')}
        </button>
      </a>
      <a class="view-code-link" href="https://github.com/RobertoVallado/cv" target="_blank" rel="nofollow">
        {$t('nav.view_source')}
      </a>
    </div>
    <div class="aside-bottom">
      <a class="get-in-touch no-underline" href="/contact">
        <i class="fa-solid fa-paper-plane"></i>
        {$t('nav.send_message')}
      </a>
      <br>
      <small class="license">
        <a href="https://github.com/RobertoVallado/cv">RobertoVallado/cv</a>
        &mdash; MIT &copy; 2025
      </small>
    </div>
  </aside>

  <div class="content-wrapper">
    <header bind:this={header}>
      <div class="nav-links">
        {#each headerLinks as { name, url }}
          <a class="no-underline" target="_blank" href={url}>{name}</a>
        {/each}
      </div>
      <div class="lang-switch">
        {#each LOCALES as l}
          <button
            class="lang-btn"
            class:active={$locale === l}
            on:click={() => setLocale(l)}
            aria-label="Switch to {l}"
          >{l.toUpperCase()}</button>
        {/each}
      </div>
    </header>

    <main bind:this={main}>
      <div class="page"><slot /></div>
    </main>
  </div>
</div>

<style lang="scss">
  .lang-switch {
    display: flex;
    gap: 0.2rem;
    margin-right: 1rem;
  }
  .lang-btn {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--text-color-dim);
    font-family: var(--font-family);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.45rem;
    border-radius: 3px;
    cursor: pointer;
    transition: all 0.2s ease;
    &:hover {
      color: var(--primary);
      border-color: var(--primary);
    }
    &.active {
      background: var(--primary-transparent);
      border-color: var(--primary);
      color: var(--primary);
    }
  }
</style>
