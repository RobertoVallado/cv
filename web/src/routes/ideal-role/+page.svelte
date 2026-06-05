<script lang="ts">
  import { t } from '$lib/i18n';

  $: values = $t('ideal_role.values') as string[];
  $: requirements = $t('ideal_role.requirements') as { lbl: string; desc: string }[];

  const navLinks = [
    { key: 'nav.intro',        url: '/intro',        icon: 'fa-address-card' },
    { key: 'nav.experience',   url: '/experience',   icon: 'fa-briefcase' },
    { key: 'nav.skills',       url: '/skills',       icon: 'fa-code' },
    { key: 'nav.achievements', url: '/achievements', icon: 'fa-star' },
  ];
</script>

<svelte:head>
  <title>{$t('ideal_role.page_title')}</title>
  <meta name="description" content="Roberto Vallado's ideal job — work values, environment preferences, and what makes a great role. Open to full-stack, security, and SEO-focused positions.">
</svelte:head>

<h1>{$t('ideal_role.h1')}</h1>

{#each ['ideal_role.p0','ideal_role.p1','ideal_role.p2'] as key}
  <p>{$t(key)}</p>
{/each}

<h2>{$t('ideal_role.values_title')}</h2>
<p class="subtitle">{$t('ideal_role.values_sub')}</p>
<ul>
  {#each values as value}
    <li>{value}</li>
  {/each}
</ul>

<h2>{$t('ideal_role.req_title')}</h2>
<p class="subtitle">{$t('ideal_role.req_sub')}</p>
<ul>
  {#each requirements as { lbl, desc }}
    <li><strong>{lbl}:</strong> {desc}</li>
  {/each}
</ul>

<h2>{$t('ideal_role.why_title')}</h2>
<p>
  {$t('ideal_role.why_text')} <a href="/intro">{$t('ideal_role.why_intro')}</a>
  {$t('ideal_role.why_mid')} <a href="/achievements">{$t('ideal_role.why_achievements')}</a>,
  {$t('ideal_role.why_end')} <a href="/contact">{$t('ideal_role.why_contact')}</a>.
</p>

<div class="other-pages">
  {#each navLinks as { key, url, icon }}
    <a href={url} class="no-underline">
      <button class="big-btn"><i class="fa-solid {icon}"></i>{$t(key)}</button>
    </a>
  {/each}
</div>

<style lang="scss">
h2 { font-size: 1.2rem; font-weight: 600; margin: 2rem 0 0.5rem 0; }
.subtitle { margin: 0 0 0.5rem 0; font-size: 0.8rem; font-style: italic; opacity: 0.8; }
ul { margin: 0; padding-left: 1rem; font-size: 1rem; li strong { font-weight: 600; } }
p { font-size: 1rem; margin: 0 0 0.5rem 0; }
.other-pages {
  display: grid; align-items: center;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 1rem; margin: 1rem 0;
  a button { margin: 0; font-size: 1rem; padding: 0.5rem; }
}
</style>
