<script lang="ts">
  import { t, locale } from '$lib/i18n';
  export let data: { work: any[] };
  const { work } = data;

  const formatDate = (d: string) => {
    if (!d || d === 'Present') return $t('experience.current');
    const [year, month] = d.split('-');
    const months = {
      en: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
      fr: ['jan.','fév.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.'],
    };
    const m = months[$locale as 'en' | 'fr'] || months.en;
    return `${m[parseInt(month, 10) - 1]} ${year}`;
  };

  $: jobs = work.map(job => ({
    ...job,
    displayPosition: $locale === 'fr' && job['position-fr'] ? job['position-fr'] : job.position,
    displayHighlights: $locale === 'fr' && job['highlights-fr'] ? job['highlights-fr'] : job.highlights,
  }));
</script>

<svelte:head>
  <title>{$t('experience.page_title')}</title>
</svelte:head>

<h1>{$t('experience.h1')}</h1>

{#each jobs as job}
  <div class="job">
    <div class="job-header">
      <div class="job-title-block">
        <h2 class="position">{job.displayPosition}</h2>
        <span class="company">{$t('experience.at')} {job.name}</span>
      </div>
      <div class="job-meta">
        <span class="dates">
          {formatDate(job.startDate)} – {formatDate(job.endDate)}
        </span>
        {#if !job.endDate || job.endDate === 'Present'}
          <span class="badge-current">{$t('experience.current')}</span>
        {/if}
      </div>
    </div>

    {#if job.displayHighlights?.length > 0}
      <ul class="highlights">
        {#each job.displayHighlights as highlight}
          <li>{highlight}</li>
        {/each}
      </ul>
    {/if}
  </div>
{/each}

<div class="page-nav">
  <a href="/intro"        class="no-underline"><button class="big-btn"><i class="fa-solid fa-address-card"></i>{$t('nav.intro')}</button></a>
  <a href="/skills"       class="no-underline"><button class="big-btn"><i class="fa-solid fa-code"></i>{$t('nav.skills')}</button></a>
  <a href="/achievements" class="no-underline"><button class="big-btn"><i class="fa-solid fa-star"></i>{$t('nav.achievements')}</button></a>
  <a href="/contact"      class="no-underline"><button class="big-btn"><i class="fa-solid fa-paper-plane"></i>{$t('nav.contact')}</button></a>
</div>

<style lang="scss">
  h1 { margin-bottom: 1.25rem; }
  .job {
    padding: 1rem 0;
    &:not(:last-child) {
      border-bottom: 1px solid color-mix(in srgb, var(--primary) 20%, transparent);
    }
  }
  .job-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .job-title-block { display: flex; flex-direction: column; gap: 0.15rem; }
  .position { font-size: 1rem; font-weight: 700; margin: 0; color: var(--text-color); }
  .company { font-size: 0.85rem; font-weight: 500; opacity: 0.65; letter-spacing: 0.02em; }
  .job-meta { display: flex; flex-direction: column; align-items: flex-end; gap: 0.25rem; }
  .dates { font-size: 0.78rem; opacity: 0.6; white-space: nowrap; }
  .badge-current {
    font-size: 0.65rem; font-weight: 600; letter-spacing: 0.05em;
    text-transform: uppercase; background: var(--primary); color: #0b0f0c;
    padding: 0.1rem 0.45rem; border-radius: 99px;
  }
  .highlights {
    margin: 0; padding-left: 1.1rem;
    li { font-size: 0.875rem; line-height: 1.6; margin: 0.2rem 0; opacity: 0.9; }
  }
  .page-nav {
    margin-top: 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 0.75rem;
    a button { margin: 0; font-size: 0.9rem; padding: 0.5rem; width: 100%; }
  }
</style>
