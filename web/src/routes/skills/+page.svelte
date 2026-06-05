<script lang="ts">
  import Language from '../../components/Language.svelte';
  import { t } from '$lib/i18n';
  export let data: { skills: { name: string; keywords: string[] }[] };
  const { skills } = data;
  $: softSkills = $t('skills.soft') as { skill: string; desc: string }[];
</script>

<svelte:head>
  <title>{$t('skills.page_title')}</title>
  <meta name="description" content="Technical skills of Roberto Vallado — C#/.NET, Python, Angular, React, TypeScript, REST APIs, AI automation, SEO, PostgreSQL, Docker, and security research tools.">
</svelte:head>

<h1>{$t('skills.h1')}</h1>
<p class="intro">{$t('skills.intro')}</p>

{#each skills as group}
  <h3>{group.name}</h3>
  <ul class="tech-list">
    {#each group.keywords as tech}
      <li><Language language={tech} /></li>
    {/each}
  </ul>
{/each}

<h3>{$t('skills.soft_title')}</h3>
<ul class="soft-skills">
  {#each softSkills as { skill, desc }}
    <li>
      <span class="skill-name">{skill}</span>
      <span class="skill-desc">{desc}</span>
    </li>
  {/each}
</ul>

<div class="note">
  <p>
    {$t('skills.note')} <a href="https://github.com/RobertoVallado" target="_blank">{$t('skills.github')}</a>.
  </p>
</div>

<style lang="scss">
  p.intro { font-size: 0.95rem; margin-bottom: 0.5rem; }
  h3 { margin: 1.25rem 0 0.5rem; }
  .tech-list {
    list-style: none; padding: 0;
    display: flex; flex-wrap: wrap; gap: 0.4rem;
    li { font-size: 0.9rem; }
  }
  .soft-skills {
    list-style: none; padding: 0;
    li {
      margin: 0.5rem 0;
      &::before { content: '✓'; margin-right: 0.5rem; color: var(--primary); }
      .skill-name { font-weight: 500; font-size: 0.95rem; }
      .skill-desc {
        display: block; font-size: 0.8rem; opacity: 0.8;
        font-style: italic; margin-left: 1.25rem;
      }
    }
  }
  .note {
    border: 2px solid var(--primary); padding: 0.25rem 0.5rem;
    margin: 1.5rem auto 1rem; border-radius: 4px;
    background: var(--primary-transparent);
    p, a { font-size: 0.8rem; }
    a { font-weight: 500; }
  }
</style>
